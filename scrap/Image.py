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


class Test:

    filePath = 'appdata/image'
    username = ''

    def createDir(self):
        fileUsernamePath = f'{self.filePath}/{self.username}'
        if not os.path.isdir(fileUsernamePath):
            os.makedirs(fileUsernamePath)

    async def requestImageAsync(self, file):
        dirs = f'{file.username}/{file.code}'
        fileUsernamePath = f'{self.filePath}/{dirs}'
        os.makedirs(fileUsernamePath, exist_ok=True)

        fpn = f'{fileUsernamePath}/{file.image_local}'
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(file.image) as res:
                    async with aiofiles.open(fpn, 'wb') as f:
                        await f.write(await res.read())
        except Exception as e:
            print(file.image, e)
            print(traceback.format_exc())


class Image:

    userId = None
    filePath = 'appdata/image'

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('Image')
            mylogger.info(f'start image : {self.user.id}')

            test = Test()
            test.username = self.user.id
            model = Model()
            model.username = self.user.id
            files = model.getFiles()

            files = [DotMap(file) for file in files]
            tasks = [test.requestImageAsync(file) for file in files]
            loop = asyncio.get_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(asyncio.wait(tasks))
            mylogger.info(f'end image success : {self.user.id}')
        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end user error : {self.user.id}')