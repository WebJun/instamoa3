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

    def setUserName(self, userName):
        self.userName = userName

    def getUser(self):
        result = ''
        try:
            response = requests.get(
                f'https://www.instagram.com/{self.userName}/')
            result = response.text
        except:
            result = 600
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
            result = 600
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


'''
내가 원하는것
requests
다음걸로 넘어가기
'''
if __name__ == '__main__':
    util = Util()
    getUserData = GetUserData()
    model = Model()
    logger = createLogger('zzzzz')

    users = util.readFile('users.json')
    users = json.loads(users)
    
    for user in users:
        try:
            logger.info(user)
            getUserData.setUserName(user)
            user = getUserData.run()
            model.saveUser(user.user)
            logger.info('success')
        except:
            logger.error('fail')
