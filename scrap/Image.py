import traceback
import os
import aiohttp
import aiofiles
import traceback
import os
import asyncio
from dotmap import DotMap  # pip install dotmap
from createLogger import createLogger
from Model import Model
from urllib.parse import urlparse


async def requestImageAsync(uri):
    parsed_uri = urlparse(uri)
    filename, _ = os.path.splitext(parsed_uri.path)
    filename = os.path.basename(filename)
    fpn = f'appdata/image/{filename}.jpg'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(uri) as res:
                async with aiofiles.open(fpn, 'wb') as f:
                    await f.write(await res.read())
    except Exception as e:
        print(uri, e)
        print(traceback.format_exc())


class Image:

    userId = None

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('Image')
            mylogger.info(f'start image : {self.user.id}')
            model = Model()
            model.username = self.user.id
            files = model.getFiles()

            urls = [file['image'] for file in files]
            tasks = [requestImageAsync(url) for url in urls]
            loop = asyncio.get_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(asyncio.wait(tasks))

        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end user error : {self.user.id}')
