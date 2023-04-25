from Util import Util
import json
from pprint import pprint
from dotmap import DotMap  # pip install dotmap
import sys

util = Util()
user = util.readFile('appdata/json/dlwlrma copy.json')
user = json.loads(user)
user = DotMap(user)

# key중에 items이 items() 메소드와 겹치는 문제
user.fitems = user.pop('items')

apple = DotMap()
apple.user = user.user

def inner(media):
    return [v.url for i,v in enumerate(media.image_versions2.candidates) if i==0]

def outer(item):
    return [inner(media) for media in item.carousel_media] if 'carousel_media' in item else inner(item)

apple.posts = [DotMap({'code':item.code,'files':outer(item)}) for item in user.fitems]
pprint(apple)

