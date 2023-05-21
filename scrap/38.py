import requests
from pprint import pprint
from dotmap import DotMap  # pip install dotmap
import json

userId = 'dlwlrma'
xIgAppID = 'aaaa'
max_id = 'bbb'

params = {
    # 'count': '50',
    'count': '33',
    'max_id': max_id,
}
headers = {
    'X-IG-App-ID': xIgAppID,
}

apple = DotMap()
apple.url = f'https://test2.cono.kr/request/{userId}/'
apple.params = params
apple.headers = headers
apple.allow_redirects = False

qqq = {
    'url': f'https://test2.cono.kr/request/{userId}/',
    'params': params,
    'headers': headers,
    'allow_redirects': False,
}

response = requests.get(
    f'https://test2.cono.kr/request/{userId}/',
    params=params,
    headers=headers,
    allow_redirects=False,
)


def requestsGet(**args):
    print(json.dumps(args))
    response = requests.get(**args)


# apple = apple.toDict()
requests.get(**apple)
