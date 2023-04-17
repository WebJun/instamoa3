import requests # pip install requests
from Util import Util
import sys
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint

headers = {
    'X-IG-App-ID': '936619743392459',
}

util = Util()
now = util.now()
response = requests.get(
    'https://www.instagram.com/api/v1/feed/user/1518940500/',
    headers=headers,
)

with open(f'appdata/json/{now}.json', 'wb') as f:
    f.write(response.content)

s = json.loads(response.content)
s = DotMap(s)

pprint(s.user)
print(s.status)
