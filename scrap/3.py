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


def aa(a):
    return [v.url for i,v in enumerate(a.image_versions2.candidates) if i==0]



apple.posts = []
for item in user.fitems:
    bb = DotMap()
    bb.code = item.code
    bb.files = []
    if 'carousel_media' in item:
        for a in item.carousel_media:
            bb.files = bb.files + aa(a)
    else:
        bb.files = bb.files + aa(item)
    apple.posts.append(bb)

pprint(apple)
# a = json.dumps(dict(apple))
# print(a)



