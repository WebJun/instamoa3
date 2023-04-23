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
user = util.readFile('appdata/json/dlwlrma.json')
user = json.loads(user)
user = dict_to_dotmap(user)

apple = DotMap()

# pprint(user)
# apple.user = user.user

# print(user.items)

# print(user['items'][0])
print(user.items[0])
# print(user.items[0])
# for item in user.items:
    # print(item)
    # apple.sss.append(item.taken_at)


# pprint(apple)

