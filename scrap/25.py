import requests # pip install requests
from Util import Util
import sys
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint

headers = {
    'X-IG-App-ID': '936619743392459',
}
params = {
    'count': '12',
    'max_id': '2968247614265925787_1692800026',
}
util = Util()
now = util.now()
response = requests.get(
    'https://www.instagram.com/api/v1/feed/user/1692800026/',
    params=params,
    headers=headers,
)
util = Util()
util.saveFile(f'{now}.json', response.text)
