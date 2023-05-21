from dotmap import DotMap  # pip install dotmap
import json
from Util import Util
import traceback
from createLogger import createLogger
import os
from GetUserData import GetUserData


class InstaCrawling:

    filePath = 'appdata/data'
    username = ''

    def __init__(self):
        self.util = Util()

    def run(self):
        fileUsernamePath = f'{self.filePath}/{self.username}'
        if not os.path.isdir(fileUsernamePath):
            os.makedirs(fileUsernamePath)

        getUserData = GetUserData()
        apple = DotMap()
        apple.username = self.username
        getUserData.setUserName(apple.username)
        getUserData.first()

        i = 0
        while True:
            user, next = getUserData.repeat()

            self.util.saveFile(
                f'{fileUsernamePath}/{self.util.now()}.json', json.dumps(user.toDict()))

            print(i, next)
            if next == False:
                break
            i = i + 1


class Http:

    userId = None

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('Http')
            insta = InstaCrawling()
            insta.username = self.user.id
            insta.run()
        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end http error : {self.user.id}')
