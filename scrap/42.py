import requests
from Util import Util

response = requests.get(
    'https://www.instagram.com/api/v1/feed/user/1692800026/',
    params={
        'count': '33',
        'max_id': '2826087862598795349_1692800026',
    },
    headers={
        'X-IG-App-ID': '936619743392459',
    },
)
# 2835060676316182557_1692800026 CdYKKoQgTgd
# 2826087862598795349_1692800026 Cc4R_ASPoBV
# 
'''
feed(post)에는 id라는게 있다
2835060676316182557_1692800026이게 그 id이다
이거를 max_id에 넣으면 그 feed 이전의 feed들을 가져온다

# 2835060676316182557_1692800026 CdYKKoQgTgd
# 2826087862598795349_1692800026 Cc4R_ASPoBV

'''
util = Util()
util.saveFile(f'{util.now()}.json', response.text)
