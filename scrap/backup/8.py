import requests # pip install requests
from Util import Util
import sys
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint

# headers = {
#     'X-IG-App-ID': '936619743392459',
# } 
if __name__ == '__main__':
    util = Util()
    now = util.now()
    response = requests.get(
        'https://www.instagram.com/dlwlrma/'
    )
    html = response.text
    util.saveFile(f'appdata/html/{now}.html', html)

    # html = util.readFile('appdata/html/20230413220515705802.html')
    user_id = util.extraxtText(html, '","user_id":"','","include_chaining"')
    print(user_id)


    headers = {
        'X-IG-App-ID': '936619743392459',
    }

    now = util.now()
    response = requests.get(
        f'https://www.instagram.com/api/v1/feed/user/{user_id}/',
        headers=headers,
    )
    json = response.text
    util.saveFile(f'appdata/json/{now}.json', json)
