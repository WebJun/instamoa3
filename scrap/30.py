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
        user = self.http.getUserJson3(self.userId, self.xIgAppID, self.max_id)
        self.max_id = user.next_max_id
        next = False
        if user.more_available:
            next = True
        return user, next


def getFilesInner(item, username, code):
    result = DotMap()
    result.username = username
    result.code = code
    result.id = item.id
    result.image = None
    result.video = None
    if 'image_versions2' in item:
        result.image = item.image_versions2.candidates[0].url
    if 'video_versions' in item:
        result.video = item.video_versions[0].url
    return result


def getFiles(item):
    username = item.user.username
    code = item.code
    if 'carousel_media' not in item:
        return [getFilesInner(item, username, code)]

    result = []
    for carousel_item in item.carousel_media:
        result.append(getFilesInner(carousel_item, username, code))
    return result


def getPosts(item):
    itemTemp = DotMap()
    itemTemp.taken_at = item.taken_at
    itemTemp.pk = item.pk
    itemTemp.id = item.id
    itemTemp.media_type = item.media_type
    itemTemp.code = item.code
    itemTemp.carousel_media_count = item.carousel_media_count if 'carousel_media_count' in item else 1
    itemTemp.comment_count = item.comment_count
    itemTemp.username = item.user.username

    if item.caption:
        itemTemp.text = item.caption.text
        itemTemp.status = item.caption.status
        itemTemp.created_at = item.caption.created_at
    else:
        itemTemp.text = ''
        itemTemp.status = ''
        itemTemp.created_at = ''
    return itemTemp


if __name__ == '__main__':
    util = Util()
    getUserData = GetUserData()
    model = Model()
    logger = createLogger('users')

    apple = DotMap()
    apple.username = 'okjayeon'
    logger.info(apple.username)
    getUserData.setUserName(apple.username)
    getUserData.first()

    i = 0
    while True:
        # for i in range(0, 3):
        user, next = getUserData.repeat()

        data = DotMap(user)

        data.fitems = data.pop('items')
        apple.user = data.user

        apple.posts = []
        for item in data.fitems:
            apple.posts.append(getPosts(item))

        apple.files = []
        for item in data.fitems:
            apple.files = apple.files + getFiles(item)

        if i == 0:
            model.saveUser(apple.user)
        model.savePosts(apple.posts)
        model.saveFiles(apple.files)
        print(i, next)
        if next == False:
            break
        i = i + 1
