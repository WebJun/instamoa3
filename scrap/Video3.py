import os
import asyncio
import aiohttp
import aiofiles
import traceback
from dotmap import DotMap
from createLogger import createLogger
from Model import Model
from Config import Config
from pprint import pprint


class Video3Downloader:
    filePath = 'appdata/Video3'
    files = []

    def __init__(self):
        self.logger = createLogger('Video3Downloader')
        config = Config()

        if config.WIFI_IP:
            self.conn = aiohttp.TCPConnector(
                local_addr=(config.WIFI_IP, 0))
        else:
            self.conn = aiohttp.TCPConnector()

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())
        return self.files

    def setFiles(self, files):
        self.files = files

    async def downloadVideo3(self, session, index):
        file = self.files[index]
        dirs = f'{file.username}/{file.code}'
        fileUsernamePath = f'{self.filePath}/{dirs}'
        os.makedirs(fileUsernamePath, exist_ok=True)
        fpn = f'{fileUsernamePath}/{file.video_local}'
        try:
            async with session.get(file.video) as response:
                async with aiofiles.open(fpn, 'wb') as f:
                    if response.status == 200:
                        while True:
                            chunk = await response.content.read(1024)
                            if not chunk:
                                break
                            await f.write(chunk)
                        file.video_status = 200
                    else:
                        file.video_status = response.status
        except asyncio.exceptions.TimeoutError as err:
            self.errorHandle(fpn, err)
            file.video_status = 400
        except aiohttp.client_exceptions.ServerDisconnectedError as err:
            self.errorHandle(fpn, err)
            file.video_status = 400
        except Exception as err:
            self.errorHandle(fpn, err)
            file.video_status = 400

    def errorHandle(self, fpn, err):
        self.logger.info(traceback.format_exc())
        self.logger.info(err)
        if os.path.isfile(fpn):
            os.remove(fpn)

    async def downloadVideo3s(self, concurrencyLimit):
        async with aiohttp.ClientSession(connector=self.conn) as session:
            semaphore = asyncio.Semaphore(concurrencyLimit)
            tasks = []
            for index, file in enumerate(self.files):
                print(index)
                async with semaphore:
                    task = asyncio.create_task(
                        self.downloadVideo3(session, index))
                    tasks.append(task)
            await asyncio.gather(*tasks)

    async def main(self):
        concurrencyLimit = 1
        await self.downloadVideo3s(concurrencyLimit)
        print('동영상 다운로드 완료')


class Video3:
    userId = None

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            myLogger = createLogger('Video3')
            myLogger.info(f'start Video3: {self.user.id}')

            model = Model()
            downloader = Video3Downloader()

            model.username = self.user.id
            files = model.getFiles()
            files = [DotMap(file) for file in files]
            files = [file for file in files if file.video is not None]

            downloader.setFiles(files)
            files = downloader.run()
            model.updateVideoFiles(files)

            myLogger.info(f'end Video3 success: {self.user.id}')
        except Exception as err:
            myLogger.info(traceback.format_exc())
            myLogger.info(err)
            myLogger.info(f'end user error: {self.user.id}')
