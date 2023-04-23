import requests  # pip install requests
from Util import Util
import sys
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint
from createLogger import createLogger
from Model import Model
from bs4 import BeautifulSoup  # pip install bs4
import traceback

class GetUserData:

    def __init__(self):
        self.util = Util()
        # self.logger = createLogger('user')
        self.logger = Util()

    def setUserName(self, userName):
        self.userName = userName

    def getUser(self):
        response = requests.get(
            f'https://www.instagram.com/{self.userName}/', allow_redirects=False, timeout=1)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code)
        if self.check404(response.text):
            raise Exception('aaaa')
        return response.text
    
    def check404(self, html):
        #a = self.util.readFile('aaa.html')
        html = BeautifulSoup(html, 'html.parser')
        title = html.find('title').string.strip()
        print(title)
        if title == 'Instagram':
            return True
        return False

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
                allow_redirects=False,
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

if __name__ == '__main__':
    util = Util()
    getUserData = GetUserData()
    #model = Model()
    logger = createLogger('users')

    users = util.readFile('users.json')
    users = json.loads(users)
    
    for user in users:
        try:
            print(user)
            logger.info(user)
            getUserData.setUserName(user)
            user = getUserData.run()
            #model.saveUser(user.user)
            logger.info('success')
        except:
            logger.error(traceback.format_exc())
            logger.error('fail')
            #sys.exit()
