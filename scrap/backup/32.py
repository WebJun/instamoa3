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
user.iitems = user.pop('items')

apple = DotMap()
apple.user = user.user

apple.posts = []
for item in user.iitems:
    pear = DotMap()
    pear.taken_at = item.taken_at
    pear.id = item.id
    pear.pk = item.pk

    apple.files = []
    for file in item.carousel_media:
        chim = DotMap()
        
        apple.chim.qqs = []
        for aaa in file.image_versions2.candidates:
            qqq = DotMap()
            qqq.aaa = aaa.width
            apple.chim.qqs.append(qqq)

        pear.chim = chim
        apple.files.append(chim)

    apple.posts.append(pear)

pprint(apple)
