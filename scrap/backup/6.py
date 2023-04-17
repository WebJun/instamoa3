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
    'https://www.instagram.com/dlwlrma/'
)
# print(response.content)
util.saveFile(f'appdata/json/{now}.html', response.text)

# s = json.loads(response.content)
# s = DotMap(s)

# pprint(s.user)
# print(s.status)
