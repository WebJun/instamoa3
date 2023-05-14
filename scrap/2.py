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
        self.logger = createLogger('user')
        self.util = Util()
        self.http = HttpHandler()
        self.parse = ParseUser()
        self.max_id = ''

    def setUserName(self, userName):
        self.userName = userName

    def first(self):
        userHtml = self.http.getUserHtml(self.userName)
        self.userId = self.parse.userId(userHtml)
        self.xIgAppID = self.parse.xIgAppID(userHtml)

    def repeat(self):
        user = self.http.getUserJson2(self.userId, self.xIgAppID, self.max_id)
        user = DotMap(json.loads(user))
        self.max_id = self.getMaxId(user)
        print(self.max_id)
        return user

    def getMaxId(self, user):
        self.util.saveFile(f'{util.now()}.json', json.dumps(user.toDict()))
        return user.next_max_id


def inner(media):
    return [v.url for i, v in enumerate(
        media.image_versions2.candidates) if i == 0]


def outer(item):
    return [inner(media)[0] for media in item.carousel_media] if 'carousel_media' in item else inner(item)


if __name__ == '__main__':
    util = Util()
    getUserData = GetUserData()
    model = Model()
    logger = createLogger('users')

    apple = DotMap()
    apple.username = 'dlwlrma'
    logger.info(apple.username)
    getUserData.setUserName(apple.username)
    getUserData.first()

    # while True:
    for i in range(0, 3):
        user = getUserData.repeat()
        user = DotMap(user)
        user.fitems = user.pop('items')
        apple.user = user.user
        apple.posts = [DotMap({**item.caption, **item})
                       for item in user.fitems if item.caption != None]
        apple.files = [DotMap({'code': item.code, 'files': outer(item)})
                       for item in user.fitems]
        if i == 0:
            model.saveUser(apple.user)
        model.savePosts(apple.username, apple.posts)
        model.saveFiles(apple.username, apple.files)
