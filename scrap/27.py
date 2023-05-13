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
        return user

if __name__ == '__main__':
    util = Util()
    getUserData = GetUserData()
    model = Model()
    logger = createLogger('users')

    # users = util.readFile('users.json')
    # users = json.loads(users)
    

    
    apple = DotMap()
    apple.userId = 'dlwlrma'
    user = 'dlwlrma'
    logger.info(user)
    getUserData.setUserName(user)
    user = getUserData.run()
    # pprint(user)

    user = DotMap(user)
    user.fitems = user.pop('items')
    apple.user = user.user
    apple.posts = [DotMap({ **item.caption, **item}) for item in user.fitems]
    apple.postIds = [item.code for item in user.fitems]
    
    def inner(media):
        a = [v.url for i,v in enumerate(media.image_versions2.candidates) if i==0]
        return a

    def outer(item):
        return [inner(media)[0] for media in item.carousel_media] if 'carousel_media' in item else inner(item)

    apple.files = [DotMap({'code':item.code,'files':outer(item)}) for item in user.fitems]
    model.saveUser(apple.user)
    model.savePosts(apple.posts)    
    model.saveFiles(apple.userId, apple.files)
    logger.info('success')

    user_id = apple.user.pks
    qq = len(apple.posts)
    max_id = apple.posts[qq-1].id
        
    headers = {
        'X-IG-App-ID': '936619743392459',
    }
    params = {
        'count': '12',
        'max_id': max_id,
    }
    now = util.now()
    response = requests.get(
        f'https://www.instagram.com/api/v1/feed/user/{user_id}/',
        params=params,
        headers=headers,
    )
    util = Util()
    util.saveFile(f'{now}.json', response.text)