import os
import asyncio
import aiohttp
import aiofiles
import traceback
from dotmap import DotMap
from createLogger import createLogger
from Model import Model


class Video3Downloader:
    filePath = 'appdata/Video3'

    def __init__(self):
        self.logger = createLogger('Video3Downloader')

    async def downloadVideo3(self, session, file):
        try:
            async with session.get(file.video) as response:
                dirs = f'{file.username}/{file.code}'
                fileUsernamePath = f'{self.filePath}/{dirs}'
                os.makedirs(fileUsernamePath, exist_ok=True)

                fpn = f'{fileUsernamePath}/{file.video_local}'
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

    async def downloadVideo3s(self, files, concurrencyLimit):
        async with aiohttp.ClientSession() as session:
            semaphore = asyncio.Semaphore(concurrencyLimit)
            tasks = []
            for file in files:
                async with semaphore:
                    task = asyncio.create_task(
                        self.downloadVideo3(session, file))
                    tasks.append(task)
            await asyncio.gather(*tasks)

    async def main(self, files):
        concurrencyLimit = 1
        await self.downloadVideo3s(files, concurrencyLimit)

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

            loop = asyncio.get_event_loop()
            loop.run_until_complete(downloader.main(files))

            myLogger.info(f'end Video3 success: {self.user.id}')
        except Exception as err:
            myLogger.info(traceback.format_exc())
            myLogger.info(err)
            myLogger.info(f'end user error: {self.user.id}')
