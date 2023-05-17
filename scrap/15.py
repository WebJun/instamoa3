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


def inner(media):
    return [v.url for i, v in enumerate(
        media.image_versions2.candidates) if i == 0]


def outer(item):
    return [inner(media)[0] for media in item.carousel_media] if 'carousel_media' in item else inner(item)


def inner2(media):
    util.saveFile(f'{util.now()}.json', json.dumps(media.toDict()))
    # return [v.url for i, v in enumerate(
    #     media.video_versions) if i == 0]


def inner3(media):
    return []
    return [v.url for i, v in enumerate(
        media.video_versions) if i == 0]


def outer2(item):
    return [inner2(media) for media in item.carousel_media] if 'carousel_media' in item else inner3(item)


if __name__ == '__main__':
    util = Util()
    user = util.readFile('20230517023027858504.json')
    user = DotMap(json.loads(user))
    # user.fitems = user.pop('items')

    # for item in user.fitems:
    #     print(item.code, item.media_type)
    #     if 'video_versions' in item:
    #         print(item.video_versions[0].url)
    #     else:
    #         pass
    #     if 'carousel_media' in item:
    #         for item2 in item.carousel_media:
    #             if 'video_versions' in item2:
    #                 print(item2.video_versions[0].url)
    #             else:
    #                 pass

    apple = DotMap()
    # user = DotMap(user)
    user.fitems = user.pop('items')
    apple.user = user.user
    apple.posts = [DotMap({**item.caption, **item})
                   for item in user.fitems if item.caption != None]
    apple.files = [DotMap({'code': item.code, 'files': outer(item)})
                   for item in user.fitems]
    apple.files2 = [DotMap({'code': item.code, 'files': outer2(item)})
                    for item in user.fitems]

    pprint(apple.files2)
    # util.saveFile('aaa.json', json.dumps(apple.toDict()))
