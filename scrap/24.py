import requests # pip install requests
from Util import Util
import sys
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint

cookies = {
    # 'ig_nrcb': '1',
    # 'mid': 'Y8kZRwALAAG8pCSeeLPLSV59nfeE',
    # 'ig_did': 'AC8B755F-5219-4F44-B23A-B29A3233A616',
    # 'datr': 'SBnJY-t_ZXTPHz4rQBun2jkI',
    # 'csrftoken': 'nG6a6yG5WwLN3s8sVe1VERh4zSgeyuNY',
    # 'ds_user_id': '44776981787',
    # 'sessionid': '44776981787%%3AQaoG5jYpSCdoT2%%3A17%%3AAYfFKZiCs93b_9ihiDItJbp4_kE_k9J7r675lLMZy_8',
    # 'rur': '"EAG\\05444776981787\\0541712758122:01f77e11274a582a10f954c5c0badc00d79c0967921214a90d439581d5ea40bcec88a139"',
}

headers = {
    'Host': 'www.instagram.com',
    # 'Connection': 'keep-alive',
    # 'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'X-IG-App-ID': '936619743392459',
    # 'X-IG-WWW-Claim': 'hmac.AR0n4azJMEogJ37_s0R2oTXWXAxSvloDOMH2Xx7eYwzgqzIP',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    # 'viewport-width': '1389',
    # 'Accept': '*/*',
    # 'X-Requested-With': 'XMLHttpRequest',
    # 'X-ASBD-ID': '198387',
    # 'X-CSRFToken': 'nG6a6yG5WwLN3s8sVe1VERh4zSgeyuNY',
    # 'sec-ch-prefers-color-scheme': 'dark',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.instagram.com/dlwlrma/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 'ig_nrcb=1; mid=Y8kZRwALAAG8pCSeeLPLSV59nfeE; ig_did=AC8B755F-5219-4F44-B23A-B29A3233A616; datr=SBnJY-t_ZXTPHz4rQBun2jkI; csrftoken=nG6a6yG5WwLN3s8sVe1VERh4zSgeyuNY; ds_user_id=44776981787; sessionid=44776981787%%3AQaoG5jYpSCdoT2%%3A17%%3AAYfFKZiCs93b_9ihiDItJbp4_kE_k9J7r675lLMZy_8; rur="EAG\\05444776981787\\0541712758122:01f77e11274a582a10f954c5c0badc00d79c0967921214a90d439581d5ea40bcec88a139"',
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
    cookies=cookies,
    headers=headers,
    # verify=False,
)

with open(f'{now}.json', 'wb') as f:
    f.write(response.content)


s = json.loads(response.content)
s = DotMap(s)

pprint(s.user)
print(s.status)
