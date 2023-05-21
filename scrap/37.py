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
from GetUserData import GetUserData
from Mapper import Mapper


if __name__ == '__main__':
    logger = createLogger('users')
    util = Util()
    getUserData = GetUserData()
    model = Model()
    mapper = Mapper()

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
            apple.posts.append(mapper.getPosts(item))

        apple.files = []
        for item in data.fitems:
            apple.files = apple.files + mapper.getFiles(item)

        if i == 0:
            model.saveUser(apple.user)
        model.savePosts(apple.posts)
        model.saveFiles(apple.files)
        print(i, next)
        if next == False:
            break
        i = i + 1
