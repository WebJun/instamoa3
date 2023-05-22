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
from Config import Config


class Image2Downloader:

    filePath = 'appdata/Image2'
    username = ''

    def __init__(self):
        config = Config()

        if config.WIFI_IP:
            self.conn = aiohttp.TCPConnector(
                local_addr=(config.WIFI_IP, 0))
        else:
            self.conn = aiohttp.TCPConnector()

    async def requestImage2Async(self, file):
        dirs = f'{file.username}/{file.code}'
        fileUsernamePath = f'{self.filePath}/{dirs}'
        os.makedirs(fileUsernamePath, exist_ok=True)

        fpn = f'{fileUsernamePath}/{file.image_local}'
        try:
            async with aiohttp.ClientSession(connector=self.conn) as session:
                async with session.get(file.image) as res:
                    async with aiofiles.open(fpn, 'wb') as f:
                        await f.write(await res.read())
        except Exception as e:
            print(traceback.format_exc())


class Image2:

    userId = None
    filePath = 'appdata/Image2'

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('Image2')
            mylogger.info(f'start Image2 : {self.user.id}')

            downloader = Image2Downloader()
            downloader.username = self.user.id
            model = Model()
            model.username = self.user.id
            files = model.getFiles()

            files = [DotMap(file) for file in files]
            tasks = [downloader.requestImage2Async(file) for file in files]
            loop = asyncio.get_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(asyncio.wait(tasks))
            mylogger.info(f'end Image2 success : {self.user.id}')
        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end user error : {self.user.id}')
