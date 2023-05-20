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


if __name__ == '__main__':
    util = Util()
    user = util.readFile('20230517023027858504.json')
    user = DotMap(json.loads(user))
    # user.fitems = user.pop('items')

    apple = DotMap()
    # user = DotMap(user)
    user.fitems = user.pop('items')
    apple.user = user.user
    apple.posts = [DotMap({**item.caption, **item})
                   for item in user.fitems if item.caption != None]

    qqq = []
    for media in user.fitems:
        ccc = DotMap({'code': media.code})
        ccc.images = []
        ccc.videos = []
        ccc.ids = []
        if 'carousel_media' in media:
            for media in media.carousel_media:
                ccc.ids.append(media.id)
                ccc.images.append(media.image_versions2.candidates[0].url)
            if 'video_versions' in media:
                ccc.ids.append(media.id)
                ccc.videos.append(media.video_versions[0].url)
            else:
                pass
        else:
            ccc.images.append(media.image_versions2.candidates[0].url)
            if 'video_versions' in media:
                ccc.ids.append(media.id)
                ccc.videos.append(media.video_versions[0].url)
        qqq.append(ccc)
    apple.files = qqq

    pprint(apple.files)
    # pprint(apple.files)
    # pprint(apple.videos)
    # util.saveFile('aaa.json', json.dumps(apple.toDict()))
