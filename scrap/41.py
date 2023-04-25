import requests
from Util import Util

response = requests.get(
    'https://www.instagram.com/api/v1/feed/user/1692800026/',
    params={
        'count': '33',
        'max_id': '2848736843682039141_1692800026',
    },
    headers={
        'X-IG-App-ID': '936619743392459',
    },
)
# 2835060676316182557_1692800026 CdYKKoQgTgd
# 2826087862598795349_1692800026 Cc4R_ASPoBV
util = Util()
util.saveFile(f'{util.now()}.json', response.text)
