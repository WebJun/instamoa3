import requests  # pip install requests
from Util import Util
import sys
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint
from createLogger import createLogger
from Model import Model

class GetUserData:

    def __init__(self):
        self.util = Util()
        # self.logger = createLogger('user')
        self.logger = Util()
        self.userName = 'bonacosmicgirls'

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

    def parseXIgAppID(self, html):
        return self.util.extraxtText(html, '":{"X-IG-App-ID":"', '"')

    def getUserJson(self, userId, xIgAppID):
        result = ''
        try:
            response = requests.get(
                f'https://www.instagram.com/api/v1/feed/user/{userId}/',
                headers={
                    'X-IG-App-ID': xIgAppID,
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
        xIgAppID = self.parseXIgAppID(userHtml)
        print(userId, xIgAppID)
        user = self.getUserJson(userId, xIgAppID)
        user = json.loads(user)
        user = DotMap(user)
        return user


if __name__ == '__main__':
    try:
        getUserData = GetUserData()
        user = getUserData.run()
            
        model = Model()
        # a = model.getUsers('ec959aee7a844f17b479fd92ed49ea6d')
        # print(a)
        user = DotMap(user.user)
        pprint(user)
        model.saveUser(user)

    except:
        print('힝')
