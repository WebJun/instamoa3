import os
import asyncio
import aiohttp
import aiofiles
import traceback
from dotmap import DotMap
from createLogger import createLogger
from Model import Model


class ImageDownloader:
    filePath = 'appdata/image2'

    async def download_image(self, session, file):
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

    async def download_images(self, files, concurrency_limit):
        async with aiohttp.ClientSession() as session:
            semaphore = asyncio.Semaphore(concurrency_limit)
            tasks = []
            for file in files:
                async with semaphore:
                    task = asyncio.create_task(
                        self.download_image(session, file))
                    tasks.append(task)
            await asyncio.gather(*tasks)

    async def main(self, files):
        concurrency_limit = 10
        await self.download_images(files, concurrency_limit)

        print('이미지 다운로드 완료')


class Image2:
    userId = None

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('Image2')
            mylogger.info(f'start Image2: {self.user.id}')

            model = Model()
            downloader = ImageDownloader()

            model.username = self.user.id
            files = model.getFiles()
            files = [DotMap(file) for file in files]

            loop = asyncio.get_event_loop()
            loop.run_until_complete(downloader.main(files))

            mylogger.info(f'end Image2 success: {self.user.id}')
        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end user error: {self.user.id}')
