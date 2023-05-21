from Util import Util
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint
from createLogger import createLogger
from Model import Model
import traceback
from Mapper import Mapper
import os


class User:

    userId = None

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('User')
            mylogger.info(f'start user : {self.user.id}')
            model = Model()
            mapper = Mapper()
            util = Util()

            directory = f'appdata/data/{self.user.id}'
            file_list = os.listdir(directory)
            for index, file_name in enumerate(file_list):
                fpn = f'appdata/data/{self.user.id}/{file_name}'
                pprint(fpn)
                data = util.readFile(fpn)
                data = DotMap(json.loads(data))

                pprint(data.user)
                if index == 0:
                    model.saveUser(data.user)
                break
            mylogger.info(f'end user success : {self.user.id}')
        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end user error : {self.user.id}')
