from Util import Util
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint
from createLogger import createLogger
from Model import Model
import traceback
from Mapper import Mapper
import os


class File:

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('File')
            mylogger.info(f'start file : {self.user.id}')
            model = Model()
            mapper = Mapper()
            util = Util()
            mapper.username = self.user.id

            directory = f'appdata/data/{self.user.id}'
            file_list = os.listdir(directory)
            for index, file_name in enumerate(file_list):
                fpn = f'appdata/data/{self.user.id}/{file_name}'
                pprint(fpn)
                data = util.readFile(fpn)
                data = DotMap(json.loads(data))

                data.fitems = data.pop('items')

                apple = DotMap()
                apple.files = []
                for item in data.fitems:
                    apple.files = apple.files + mapper.getFiles(item)

                model.saveFiles(apple.files)
            mylogger.info(f'end file success : {self.user.id}')
        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end user error : {self.user.id}')
