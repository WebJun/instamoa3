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
        a = DotMap({'code': media.code})
        ccc = []
        if 'carousel_media' in media:
            for media in media.carousel_media:
                for i, v in enumerate(media.image_versions2.candidates):
                    if i == 0:
                        ccc.append(v.url)
            a.files = ccc
        else:
            for i, v in enumerate(media.image_versions2.candidates):
                if i == 0:
                    ccc.append(v.url)
            a.files = ccc
        qqq.append(a)
    apple.files = qqq

    sss = []
    for item in user.fitems:
        ccc = DotMap({'code': item.code})
        ccc.files2 = []
        # print(item.code, item.media_type)
        if 'video_versions' in item:
            ccc.files2.append(item.video_versions[0].url)
        else:
            pass
        if 'carousel_media' in item:
            for item2 in item.carousel_media:
                if 'video_versions' in item2:
                    ccc.files2.append(item2.video_versions[0].url)
                else:
                    pass
        sss.append(ccc)
    apple.files2 = sss

    pprint(apple.files)
    # util.saveFile('aaa.json', json.dumps(apple.toDict()))
