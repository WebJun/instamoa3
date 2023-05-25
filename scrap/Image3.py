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


class Image3Downloader:
    filePath = 'appdata/Image3'
    files = []

    def __init__(self):
        self.logger = createLogger('Image3Downloader')
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

    async def downloadImage3(self, session, index):
        file = self.files[index]
        dirs = f'{file.username}/{file.code}'
        fileUsernamePath = f'{self.filePath}/{dirs}'
        os.makedirs(fileUsernamePath, exist_ok=True)
        fpn = f'{fileUsernamePath}/{file.image_local}'
        try:
            async with session.get(file.image) as response:
                async with aiofiles.open(fpn, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        await f.write(chunk)
                    file.image_status = 200
        except asyncio.exceptions.TimeoutError as err:
            self.errorHandle(fpn, err)
            file.image_status = 400
        except aiohttp.client_exceptions.ServerDisconnectedError as err:
            self.errorHandle(fpn, err)
            file.image_status = 400
        except Exception as err:
            self.errorHandle(fpn, err)
            file.image_status = 400

    def errorHandle(self, fpn, err):
        self.logger.info(traceback.format_exc())
        self.logger.info(err)
        if os.path.isfile(fpn):
            os.remove(fpn)

    async def downloadImage3s(self, concurrencyLimit):
        async with aiohttp.ClientSession(connector=self.conn) as session:
            semaphore = asyncio.Semaphore(concurrencyLimit)
            tasks = []
            for index, file in enumerate(self.files):
                print(index)
                async with semaphore:
                    task = asyncio.create_task(
                        self.downloadImage3(session, index))
                    tasks.append(task)
            await asyncio.gather(*tasks)

    async def main(self):
        concurrencyLimit = 10
        await self.downloadImage3s(concurrencyLimit)
        print('이미지 다운로드 완료')


class Image3:
    userId = None

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            myLogger = createLogger('Image3')
            myLogger.info(f'start Image3: {self.user.id}')

            model = Model()
            downloader = Image3Downloader()

            model.username = self.user.id
            files = model.getFiles()
            files = [DotMap(file) for file in files]

            downloader.setFiles(files)
            files = downloader.run()
            model.updateImageFiles(files)

            myLogger.info(f'end Image3 success: {self.user.id}')
        except Exception as err:
            myLogger.info(traceback.format_exc())
            myLogger.info(err)
            myLogger.info(f'end user error: {self.user.id}')
