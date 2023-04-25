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

apple.posts = []
for item in user.fitems:
    bb = DotMap()
    bb.code = item.code
    bb.files = []
    if 'carousel_media' in item:
        for a in item.carousel_media:
            dd = []
            for i,v in enumerate(a.image_versions2.candidates):
                if i==0:
                    dd.append(v.url)
            bb.files.append(dd)
    else:
        for i,v in enumerate(item.image_versions2.candidates):
            if i==0:
                dd.append(v.url)
        bb.files.append(dd)
    apple.posts.append(bb)

pprint(apple)
# a = json.dumps(dict(apple))
# print(a)



