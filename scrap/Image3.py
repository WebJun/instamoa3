import os
import asyncio
import aiohttp
import aiofiles
import traceback
from dotmap import DotMap
from createLogger import createLogger
from Model import Model
from Config import Config


class Image3Downloader:
    filePath = 'appdata/Image3'

    def __init__(self):
        self.logger = createLogger('Image3Downloader')
        config = Config()

        if config.WIFI_IP:
            self.conn = aiohttp.TCPConnector(
                local_addr=(self.c.scrapServer.ip, 0))
        else:
            self.conn = aiohttp.TCPConnector()

    async def downloadImage3(self, session, file):
        try:
            async with session.get(file.image) as response:
                dirs = f'{file.username}/{file.code}'
                fileUsernamePath = f'{self.filePath}/{dirs}'
                os.makedirs(fileUsernamePath, exist_ok=True)

                fpn = f'{fileUsernamePath}/{file.image_local}'
                async with aiofiles.open(fpn, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        await f.write(chunk)
        except asyncio.exceptions.TimeoutError as err:
            self.logger.info(traceback.format_exc())
            self.logger.info(err)
        except aiohttp.client_exceptions.ServerDisconnectedError as err:
            self.logger.info(traceback.format_exc())
            self.logger.info(err)
        except Exception as err:
            self.logger.info(traceback.format_exc())
            self.logger.info(err)

    async def downloadImage3s(self, files, concurrencyLimit):
        async with aiohttp.ClientSession(connector=self.conn) as session:
            semaphore = asyncio.Semaphore(concurrencyLimit)
            tasks = []
            for file in files:
                async with semaphore:
                    task = asyncio.create_task(
                        self.downloadImage3(session, file))
                    tasks.append(task)
            await asyncio.gather(*tasks)

    async def main(self, files):
        concurrencyLimit = 1
        await self.downloadImage3s(files, concurrencyLimit)

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

            loop = asyncio.get_event_loop()
            loop.run_until_complete(downloader.main(files))

            myLogger.info(f'end Image3 success: {self.user.id}')
        except Exception as err:
            myLogger.info(traceback.format_exc())
            myLogger.info(err)
            myLogger.info(f'end user error: {self.user.id}')
