import requests
from Util import Util

cookies = {
    'ig_nrcb': '1',
    'mid': 'Y8kZRwALAAG8pCSeeLPLSV59nfeE',
    'ig_did': 'AC8B755F-5219-4F44-B23A-B29A3233A616',
    'datr': 'SBnJY-t_ZXTPHz4rQBun2jkI',
    'csrftoken': 'nG6a6yG5WwLN3s8sVe1VERh4zSgeyuNY',
    'ds_user_id': '44776981787',
    'sessionid': '44776981787%%3AQaoG5jYpSCdoT2%%3A17%%3AAYdVcRXz9H46K6yp1gi-WBH_Kf0uYgR7zsGxWy5wLms',
    'rur': '"CCO\\05444776981787\\0541713725941:01f729fa1a474b4995c2478c0910c28e1f0a829eb566e34377934b623baa09765aa2d2bf"',
}

headers = {
    'Host': 'www.instagram.com',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'X-IG-App-ID': '936619743392459',
    'X-IG-WWW-Claim': 'hmac.AR0n4azJMEogJ37_s0R2oTXWXAxSvloDOMH2Xx7eYwzgq4i1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'viewport-width': '1578',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'X-ASBD-ID': '198387',
    'X-CSRFToken': 'nG6a6yG5WwLN3s8sVe1VERh4zSgeyuNY',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.instagram.com/p/CfVx-zFvcg7/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 'ig_nrcb=1; mid=Y8kZRwALAAG8pCSeeLPLSV59nfeE; ig_did=AC8B755F-5219-4F44-B23A-B29A3233A616; datr=SBnJY-t_ZXTPHz4rQBun2jkI; csrftoken=nG6a6yG5WwLN3s8sVe1VERh4zSgeyuNY; ds_user_id=44776981787; sessionid=44776981787%%3AQaoG5jYpSCdoT2%%3A17%%3AAYdVcRXz9H46K6yp1gi-WBH_Kf0uYgR7zsGxWy5wLms; rur="CCO\\05444776981787\\0541713725941:01f729fa1a474b4995c2478c0910c28e1f0a829eb566e34377934b623baa09765aa2d2bf"',
}

params = {
    'can_support_threading': 'true',
    'permalink_enabled': 'false',
}

response = requests.get(
    'https://www.instagram.com/api/v1/media/2870420157262317627/comments/',
    params=params,
    cookies=cookies,
    headers=headers,
    verify=False,
)

util = Util()
util.saveFile('bbb.html', response.text)

