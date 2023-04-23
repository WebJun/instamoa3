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
from HttpHandler import HttpHandler


class ParseUser:
    
    def __init__(self):
        self.util = Util()

    def userId(self, html):
        result = self.util.extraxtText(html, '","user_id":"',
                                     '","include_chaining"')
        if result == '':
            raise Exception('힝1')
        return result

    def xIgAppID(self, html):
        result = self.util.extraxtText(html, '":{"X-IG-App-ID":"', '"')
        if result == '':
            raise Exception('힝2')
        return result

class GetUserData:

    def __init__(self):
        self.util = Util()
        self.logger = createLogger('user')
        self.http = HttpHandler()
        self.parse = ParseUser()

    def setUserName(self, userName):
        self.userName = userName

    def run(self):
        userHtml = self.http.getUserHtml(self.userName)
        userId = self.parse.userId(userHtml)
        xIgAppID = self.parse.xIgAppID(userHtml)
        self.logger.info(userId)
        self.logger.info(xIgAppID)
        user = self.http.getUserJson(userId, xIgAppID)
        user = DotMap(json.loads(user))
        self.logger.info(user.user)
        return user.user

if __name__ == '__main__':
    util = Util()
    getUserData = GetUserData()
    model = Model()
    logger = createLogger('users')

    # users = util.readFile('users.json')
    # users = json.loads(users)
    
    user = 'dlwlrma'
    logger.info(user)
    getUserData.setUserName(user)
    user = getUserData.run()
    model.saveUser(user)
    logger.info('success')
