from Util import Util
import sys
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint
from createLogger import createLogger
from Model import Model
from bs4 import BeautifulSoup  # pip install bs4
import traceback
from HttpHandler import HttpHandler
import aiohttp
import aiofiles
from urllib.parse import urlparse
import traceback
import os
import asyncio


class ParseUser:

    def __init__(self):
        self.util = Util()

    def userId(self, html):
        result = self.util.extraxtText(html, '","user_id":"',
                                       '","include_chaining"')
        if result == '':
            raise Exception('힝1')
        return result

    def xIgAppID(self, html):
        result = self.util.extraxtText(html, '":{"X-IG-App-ID":"', '"')
        if result == '':
            raise Exception('힝2')
        return result


class GetUserData:

    def __init__(self):
        self.logger = createLogger('user')
        self.util = Util()
        self.http = HttpHandler()
        self.parse = ParseUser()
        self.max_id = ''

    def setUserName(self, userName):
        self.userName = userName

    def first(self):
        userHtml = self.http.getUserHtml(self.userName)
        self.userId = self.parse.userId(userHtml)
        self.xIgAppID = self.parse.xIgAppID(userHtml)

    def repeat(self):
        user = self.http.getUserJson2(self.userId, self.xIgAppID, self.max_id)
        user = DotMap(json.loads(user))
        self.max_id = self.getMaxId(user)
        print(self.max_id)
        return user

    def getMaxId(self, user):
        self.util.saveFile(f'{util.now()}.json', json.dumps(user.toDict()))
        return user.next_max_id


def inner(media):
    return [v.url for i, v in enumerate(
        media.image_versions2.candidates) if i == 0]


def outer(item):
    return [inner(media)[0] for media in item.carousel_media] if 'carousel_media' in item else inner(item)


async def requestImgAsync(uri):
    parsed_uri = urlparse(uri)
    filename, _ = os.path.splitext(parsed_uri.path)
    filename = os.path.basename(filename)
    fpn = f'appdata/test/{filename}.jpg'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(uri) as res:
                async with aiofiles.open(fpn, 'wb') as f:
                    await f.write(await res.read())
    except Exception as e:
        print(uri, 9972)
        print(traceback.format_exc())

if __name__ == '__main__':
    util = Util()
    getUserData = GetUserData()
    model = Model()
    logger = createLogger('users')

    apple = DotMap()
    apple.username = 'dlwlrma'
    logger.info(apple.username)
    getUserData.setUserName(apple.username)
    files = model.getFiles()
    urls = [file['image'] for file in files]

    tasks = [requestImgAsync(url) for url in urls]
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.wait(tasks))
