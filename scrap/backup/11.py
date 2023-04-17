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
        self.userName = 'dlwlrma'

    def getUser(self):
        result = ''
        try:
            response = requests.get(
                f'https://www.instagram.com/{self.userName}/')
            result = response.text
        except:
            result = '실패'
        self.logger.info(result)
        return result

    def parseUserId(self, html):
        return self.util.extraxtText(html, '","user_id":"',
                                     '","include_chaining"')

    def getUserJson(self, userId):
        result = ''
        try:
            response = requests.get(
                f'https://www.instagram.com/api/v1/feed/user/{userId}/',
                headers={
                    'X-IG-App-ID': '936619743392459',
                },
            )
            result = response.text
        except:
            result = '실패'
        self.logger.info(result)
        return result

    def run(self):
        userHtml = self.getUser()
        userId = self.parseUserId(userHtml)
        user = self.getUserJson(userId)
        user = json.loads(user)
        user = DotMap(user)
        return user
        #


if __name__ == '__main__':
    try:
        getUserData = GetUserData()
        user = getUserData.run()
        pprint(user.user.full_name)
        pprint(user.user.pk_id)
    except:
        print('힝')
