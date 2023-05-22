import traceback
import os
import aiohttp
import aiofiles
import traceback
import os
import sys
import asyncio
from dotmap import DotMap  # pip install dotmap
from createLogger import createLogger
from Model import Model
from urllib.parse import urlparse
from pprint import pprint


class Video2Downloader:

    filePath = 'appdata/Video2'
    username = ''

    async def requestVideo2Async(self, file):
        dirs = f'{file.username}/{file.code}'
        fileUsernamePath = f'{self.filePath}/{dirs}'
        os.makedirs(fileUsernamePath, exist_ok=True)

        fpn = f'{fileUsernamePath}/{file.video_local}'
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(file.video) as res:
                    async with aiofiles.open(fpn, 'wb') as f:
                        await f.write(await res.read())
        except Exception as e:
            print(traceback.format_exc())


class Video2:

    userId = None
    filePath = 'appdata/Video2'

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('Video2')
            mylogger.info(f'start Video2 : {self.user.id}')

            downloader = Video2Downloader()
            downloader.username = self.user.id
            model = Model()
            model.username = self.user.id
            files = model.getFiles()

            files = [DotMap(file) for file in files]
            files = [file for file in files if file.video is not None]
            tasks = [downloader.requestVideo2Async(file) for file in files]
            loop = asyncio.get_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(asyncio.wait(tasks))
            mylogger.info(f'end Video2 success : {self.user.id}')
        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end user error : {self.user.id}')
