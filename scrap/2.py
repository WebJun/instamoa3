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

apple.posts = list(map(lambda item: (
    bb := DotMap(code=item.code, files=[
        dd := [
            v.url for i, v in enumerate(item.image_versions2.candidates) if i == 0
        ]
    ] if 'carousel_media' in item else [
        dd := [
            v.url for i, v in enumerate(item.image_versions2.candidates) if i == 0
        ]
    ])
), user.fitems))

pprint(apple)
# a = json.dumps(dict(apple))
# print(a)



