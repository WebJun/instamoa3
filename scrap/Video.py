import traceback
import os
import traceback
import os
import requests
from dotmap import DotMap  # pip install dotmap
from createLogger import createLogger
from Model import Model
from urllib.parse import urlparse


class Video:

    userId = None

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('Video')
            mylogger.info(f'start video : {self.user.id}')
            model = Model()
            model.username = self.user.id

            files = model.getFiles()
            urls = [file['video'] for file in files if file['video'] != None]
            for i, url in enumerate(urls):
                parsed_uri = urlparse(url)
                filename, _ = os.path.splitext(parsed_uri.path)
                filename = os.path.basename(filename)
                save_path = f'appdata/video/{filename}.mp4'
                response = requests.get(url, timeout=60000)
                with open(save_path, 'wb') as f:
                    f.write(response.content)

        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end user error : {self.user.id}')
