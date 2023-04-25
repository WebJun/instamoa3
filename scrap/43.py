import requests
from Util import Util

response = requests.get(
    'https://www.instagram.com/api/v1/feed/user/1692800026/',
    params={
        'count': '33',
        'max_id': '2527108403668315737_1692800026',
    },
    headers={
        'X-IG-App-ID': '936619743392459',
    },
)

util = Util()
util.saveFile(f'{util.now()}.json', response.text)
