import traceback
import os
import traceback
import os
import requests
from dotmap import DotMap  # pip install dotmap
from createLogger import createLogger
from Model import Model
from urllib.parse import urlparse


class Test:

    filePath = 'appdata/video'
    username = ''

    def requestVideoSync(self, files):
        for i, file in enumerate(files):
            dirs = f'{file.username}/{file.code}'
            fileUsernamePath = f'{self.filePath}/{dirs}'
            os.makedirs(fileUsernamePath, exist_ok=True)

            fpn = f'{fileUsernamePath}/{file.video_local}'
            print(fpn)
            with open(fpn, 'wb') as f:
                response = requests.get(file.video)
                f.write(response.content)


class Video:

    userId = None

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('Video')
            mylogger.info(f'start video : {self.user.id}')

            test = Test()
            test.username = self.user.id
            model = Model()
            model.username = self.user.id
            files = model.getFiles()

            files = [DotMap(file) for file in files]
            files = [file for file in files if file.video != None]
            test.requestVideoSync(files)
            mylogger.info(f'end video success : {self.user.id}')
        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end user error : {self.user.id}')
