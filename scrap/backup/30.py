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


user.qqq = user.pop("items")

# print(user.items)
print(user.qqq[0])


# print(user.qqq[0])

# for a in list(user.items):
    # print(a)

# for p in enumerate(t):

