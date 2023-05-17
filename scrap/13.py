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

if __name__ == '__main__':
    util = Util()
    user = util.readFile('20230517023027858504.json')
    user = DotMap(json.loads(user))
    user.fitems = user.pop('items')

    for item in user.fitems:
        if 'video_versions' in item:
            print(item.video_versions[0].url)
        else:
            pass
        if 'carousel_media' in item:
            for item2 in item.carousel_media:
                if 'video_versions' in item2:
                    print(item2.video_versions[0].url)
                else:
                    pass
