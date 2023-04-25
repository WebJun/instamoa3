from Util import Util
import json
from pprint import pprint
from dotmap import DotMap  # pip install dotmap

def dict_to_dotmap(d):
    dotmap = DotMap()
    for key, value in d.items():
        if isinstance(value, dict):
            value = dict_to_dotmap(value)
        elif isinstance(value, list):
            value = [dict_to_dotmap(v) if isinstance(v, dict) else v for v in value]
        dotmap[key] = value
    return dotmap

util = Util()
user = util.readFile('appdata/json/dlwlrma copy.json')
user = json.loads(user)
user = DotMap(user)

# key중에 items이 items() 메소드와 겹치는 문제
user.fitems = user.pop('items')

apple = DotMap()
apple.user = user.user
apple.posts = [item.code for item in user.fitems]
apple.files = [v.url for item in user.fitems for a in item.carousel_media for i,v in enumerate(a.image_versions2.candidates) if i==0]

pprint(apple)
pprint(len(apple.files))