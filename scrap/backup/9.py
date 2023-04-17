import requests  # pip install requests
from Util import Util
import sys
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint
from createLogger import createLogger


class GetUserData:

    def __init__(self):
        self.util = Util()
        self.logger = createLogger('user')

    def run(self):
        userName = 'dlwlrma'
        response = requests.get(f'https://www.instagram.com/{userName}/')
        self.logger.info(response.text)
        user_id = self.util.extraxtText(response.text, '","user_id":"',
                                        '","include_chaining"')
        pprint(user_id)
        headers = {
            'X-IG-App-ID':
            '936619743392459',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }
        response = requests.get(
            f'https://www.instagram.com/api/v1/feed/user/{user_id}/',
            headers=headers,
        )
        self.logger.info(response.text)


if __name__ == '__main__':
    try:
        getUserData = GetUserData()
        user = getUserData.run()
        print(user)
    except:
        print('힝')
