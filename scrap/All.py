import json
import traceback
import os
import asyncio
import aiohttp
import aiofiles
from dotmap import DotMap  # pip install dotmap
from Util import Util
from createLogger import createLogger
from GetUserData import GetUserData
from Util import Util
from Model import Model
from Mapper import Mapper
from pprint import pprint


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
            break


class Image3Downloader:
    filePath = 'appdata/Image3'
    files = []

    def __init__(self):
        self.logger = createLogger('Image3Downloader')
        config = Config()

        if config.WIFI_IP:
            self.conn = aiohttp.TCPConnector(
                local_addr=(config.WIFI_IP, 0))
        else:
            self.conn = aiohttp.TCPConnector()

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())
        return self.files

    def setFiles(self, files):
        self.files = files

    async def downloadImage3(self, session, index):
        file = self.files[index]
        dirs = f'{file.username}/{file.code}'
        fileUsernamePath = f'{self.filePath}/{dirs}'
        os.makedirs(fileUsernamePath, exist_ok=True)
        fpn = f'{fileUsernamePath}/{file.image_local}'
        try:
            async with session.get(file.image) as response:
                async with aiofiles.open(fpn, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        await f.write(chunk)
                    file.image_status = 200
        except asyncio.exceptions.TimeoutError as err:
            self.errorHandle(fpn, err)
            file.image_status = 400
        except aiohttp.client_exceptions.ServerDisconnectedError as err:
            self.errorHandle(fpn, err)
            file.image_status = 400
        except Exception as err:
            self.errorHandle(fpn, err)
            file.image_status = 400

    def errorHandle(self, fpn, err):
        self.logger.info(traceback.format_exc())
        self.logger.info(err)
        if os.path.isfile(fpn):
            os.remove(fpn)

    async def downloadImage3s(self, concurrencyLimit):
        async with aiohttp.ClientSession(connector=self.conn) as session:
            semaphore = asyncio.Semaphore(concurrencyLimit)
            tasks = []
            for index, file in enumerate(self.files):
                print(index)
                async with semaphore:
                    task = asyncio.create_task(
                        self.downloadImage3(session, index))
                    tasks.append(task)
            await asyncio.gather(*tasks)

    async def main(self):
        concurrencyLimit = 10
        await self.downloadImage3s(concurrencyLimit)
        print('이미지 다운로드 완료')


class Video3Downloader:
    filePath = 'appdata/Video3'
    files = []

    def __init__(self):
        self.logger = createLogger('Video3Downloader')
        config = Config()

        if config.WIFI_IP:
            self.conn = aiohttp.TCPConnector(
                local_addr=(config.WIFI_IP, 0))
        else:
            self.conn = aiohttp.TCPConnector()

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())
        return self.files

    def setFiles(self, files):
        self.files = files

    async def downloadVideo3(self, session, index):
        file = self.files[index]
        dirs = f'{file.username}/{file.code}'
        fileUsernamePath = f'{self.filePath}/{dirs}'
        os.makedirs(fileUsernamePath, exist_ok=True)
        fpn = f'{fileUsernamePath}/{file.video_local}'
        try:
            async with session.get(file.video) as response:
                async with aiofiles.open(fpn, 'wb') as f:
                    if response.status == 200:
                        while True:
                            chunk = await response.content.read(1024)
                            if not chunk:
                                break
                            await f.write(chunk)
                        file.video_status = 200
                    else:
                        file.video_status = response.status
        except asyncio.exceptions.TimeoutError as err:
            self.errorHandle(fpn, err)
            file.video_status = 400
        except aiohttp.client_exceptions.ServerDisconnectedError as err:
            self.errorHandle(fpn, err)
            file.video_status = 400
        except Exception as err:
            self.errorHandle(fpn, err)
            file.video_status = 400

    def errorHandle(self, fpn, err):
        self.logger.info(traceback.format_exc())
        self.logger.info(err)
        if os.path.isfile(fpn):
            os.remove(fpn)

    async def downloadVideo3s(self, concurrencyLimit):
        async with aiohttp.ClientSession(connector=self.conn) as session:
            semaphore = asyncio.Semaphore(concurrencyLimit)
            tasks = []
            for index, file in enumerate(self.files):
                print(index)
                async with semaphore:
                    task = asyncio.create_task(
                        self.downloadVideo3(session, index))
                    tasks.append(task)
            await asyncio.gather(*tasks)

    async def main(self):
        concurrencyLimit = 1
        await self.downloadVideo3s(concurrencyLimit)
        print('동영상 다운로드 완료')


class All:

    userId = None

    def __init__(self, userId):
        self.user = DotMap()
        self.user.id = userId

    def run(self):
        try:
            mylogger = createLogger('All')
            mylogger.info(f'start all : {self.user.id}')
            insta = InstaCrawling()
            '''
            kimviju
            clairehauyo
            tsu_chan44rika
            cher_e
            evieleemikomin
            leuwsii
            '''
            insta.username = self.user.id
            insta.run()

            ###################################################################
            ###################################################################
            ###################################################################
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

            ###################################################################
            ###################################################################
            ###################################################################
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
                apple.posts = []
                for item in data.fitems:
                    apple.posts.append(mapper.getPosts(item))

                model.savePosts(apple.posts)
                break
            ###################################################################
            ###################################################################
            ###################################################################
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
                break
            ###################################################################
            ###################################################################
            ###################################################################

            model = Model()
            downloader = Image3Downloader()

            model.username = self.user.id
            files = model.getFiles()
            files = [DotMap(file) for file in files]

            downloader.setFiles(files)
            files = downloader.run()
            model.updateImageFiles(files)
            ###################################################################
            ###################################################################
            ###################################################################

            model = Model()
            downloader = Video3Downloader()

            model.username = self.user.id
            files = model.getFiles()
            files = [DotMap(file) for file in files]
            files = [file for file in files if file.video is not None]

            downloader.setFiles(files)
            files = downloader.run()
            model.updateVideoFiles(files)

            ###################################################################
            ###################################################################
            ###################################################################

            mylogger.info(f'end all success : {self.user.id}')
        except Exception as err:
            mylogger.info(traceback.format_exc())
            mylogger.info(err)
            mylogger.info(f'end all error : {self.user.id}')
