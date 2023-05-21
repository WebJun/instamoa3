from Util import Util
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint
from createLogger import createLogger
from Model import Model
import traceback
from Mapper import Mapper
import os


class Post:

    userId = None

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('Post')
            mylogger.info(f'start post : {self.user.id}')
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

                data.fitems = data.pop('items')
                apple = DotMap()
                apple.posts = []
                for item in data.fitems:
                    apple.posts.append(mapper.getPosts(item))

                model.savePosts(apple.posts)

        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end user error : {self.user.id}')
