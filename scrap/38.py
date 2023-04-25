import requests
from Util import Util

cookies = {
    'ig_nrcb': '1',
    'mid': 'Y8kZRwALAAG8pCSeeLPLSV59nfeE',
    'ig_did': 'AC8B755F-5219-4F44-B23A-B29A3233A616',
    'datr': 'SBnJY-t_ZXTPHz4rQBun2jkI',
    'csrftoken': 'nG6a6yG5WwLN3s8sVe1VERh4zSgeyuNY',
    'ds_user_id': '44776981787',
    'sessionid': '44776981787%%3AQaoG5jYpSCdoT2%%3A17%%3AAYfkX6gGMjmJ4KmWaUnvJhWw1anRfrcRnX9L6Q77DXA',
    'rur': '"EAG\\05444776981787\\0541713805893:01f7622fc67a4f5d44bb87229400bdeb3e843088bfd6d2952b35d251e0dd6f53e34d6725"',
}

headers = {
    'Host': 'www.instagram.com',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'X-IG-App-ID': '936619743392459',
    'X-IG-WWW-Claim': 'hmac.AR0n4azJMEogJ37_s0R2oTXWXAxSvloDOMH2Xx7eYwzgq7L6',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'viewport-width': '1920',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'X-ASBD-ID': '198387',
    'X-CSRFToken': 'nG6a6yG5WwLN3s8sVe1VERh4zSgeyuNY',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.instagram.com/dlwlrma/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 'ig_nrcb=1; mid=Y8kZRwALAAG8pCSeeLPLSV59nfeE; ig_did=AC8B755F-5219-4F44-B23A-B29A3233A616; datr=SBnJY-t_ZXTPHz4rQBun2jkI; csrftoken=nG6a6yG5WwLN3s8sVe1VERh4zSgeyuNY; ds_user_id=44776981787; sessionid=44776981787%%3AQaoG5jYpSCdoT2%%3A17%%3AAYfkX6gGMjmJ4KmWaUnvJhWw1anRfrcRnX9L6Q77DXA; rur="EAG\\05444776981787\\0541713805893:01f7622fc67a4f5d44bb87229400bdeb3e843088bfd6d2952b35d251e0dd6f53e34d6725"',
}

params = {
    'count': '12',
    'max_id': '2981250059863657882_1692800026',
}

response = requests.get(
    'https://www.instagram.com/api/v1/feed/user/1692800026/',
    params=params,
    cookies=cookies,
    headers=headers,
    verify=False,
)

util = Util()
util.saveFile(f'{util.now()}.json', response.text)
