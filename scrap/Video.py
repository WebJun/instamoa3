import traceback
import os
import traceback
import sys
import requests
from dotmap import DotMap  # pip install dotmap
from createLogger import createLogger
from Model import Model
from urllib.parse import urlparse
from Config import Config
from pprint import pprint


class VideoDownloader:

    filePath = 'appdata/Video'
    username = ''

    def __init__(self):
        config = Config()

        if config.WIFI_IP:
            self.requests = self.session_for_src_addr(config.WIFI_IP)
        else:
            self.requests = requests

    def session_for_src_addr(self, nic):
        session = requests.Session()
        for prefix in ('http://', 'https://'):
            session.get_adapter(prefix).init_poolmanager(
                connections=requests.adapters.DEFAULT_POOLSIZE,
                maxsize=requests.adapters.DEFAULT_POOLSIZE,
                source_address=(nic, 0),
            )
        return session

    def requestVideoSync(self, files):
        for index, file in enumerate(files):
            pprint(index)
            dirs = f'{file.username}/{file.code}'
            fileUsernamePath = f'{self.filePath}/{dirs}'
            os.makedirs(fileUsernamePath, exist_ok=True)
            fpn = f'{fileUsernamePath}/{file.video_local}'
            try:
                with open(fpn, 'wb') as f:
                    response = self.requests.get(file.video)
                    f.write(response.content)
                    file.video_status = 200
            except Exception as err:
                if os.path.isfile(fpn):
                    os.remove(fpn)
                file.video_status = 400
        return files


class Video:

    userId = None

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('Video')
            mylogger.info(f'start Video : {self.user.id}')

            downloader = VideoDownloader()
            downloader.username = self.user.id
            model = Model()
            model.username = self.user.id
            files = model.getFiles()

            files = [DotMap(file) for file in files]
            files = [file for file in files if file.video is not None]
            files = downloader.requestVideoSync(files)
            model.updateVideoFiles(files)
            mylogger.info(f'end Video success : {self.user.id}')
        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end user error : {self.user.id}')
