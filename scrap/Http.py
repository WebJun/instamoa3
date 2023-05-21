from dotmap import DotMap  # pip install dotmap
import time
import json
import sys
import logging
from Util import Util
from Model import Model
from IpManager import IpManager
import traceback
from createLogger import createLogger
import os


class InstaCrawling:

    filePath = 'appdata/data'
    username = ''

    def __init__(self):
        self.util = Util()

    def run(self):
        if not os.path.isdir(f'{self.filePath}/{self.username}'):
            os.makedirs(f'{self.filePath}/{self.username}')

        self.util.saveFile(
            f'{self.filePath}/{self.username}/{self.util.now()}.json', '1')


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
            mylogger.info(f'end user error : {self.user.id}')
