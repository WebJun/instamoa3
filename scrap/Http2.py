from dotmap import DotMap  # pip install dotmap
import json
from Util import Util
import traceback
from createLogger import createLogger
from Model import Model
import os
from GetUserData import GetUserData
from pprint import pprint


class InstaCrawling:

    filePath = 'appdata/data'
    username = ''

    def __init__(self):
        self.util = Util()
        self.getUserData = GetUserData()

    def first(self):
        fileUsernamePath = f'{self.filePath}/{self.username}'
        if not os.path.isdir(fileUsernamePath):
            os.makedirs(fileUsernamePath)

        apple = DotMap()
        apple.username = self.username
        self.getUserData.setUserName(apple.username)
        self.getUserData.first()

    def repeat(self):
        return self.getUserData.repeat()


class Http2:

    userId = None

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('Http2')
            mylogger.info(f'start http2 : {self.user.id}')

            insta = InstaCrawling()
            insta.username = self.user.id
            insta.first()

            model = Model()
            model.username = self.user.id

            while True:
                user, next = insta.repeat()
                model.saveUserfeed(user)
                if next:
                    break

            mylogger.info(f'end http2 success : {self.user.id}')
        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end http2 error : {self.user.id}')
