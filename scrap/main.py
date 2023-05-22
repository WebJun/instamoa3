import sys
from Http import Http
from User import User
from Post import Post
from File import File
from Image import Image
from Image2 import Image2
from Video import Video
from Video2 import Video2
import json
from createLogger import createLogger


class InstaFactory:

    logger = None

    def __init__(self, logger):
        self.logger = logger

    def create(self, argv):
        self.logger.info(json.dumps(argv))
        try:
            if argv[1] == 'http':
                return Http(argv[2])
            elif argv[1] == 'user':
                return User(argv[2])
            elif argv[1] == 'post':
                return Post(argv[2])
            elif argv[1] == 'file':
                return File(argv[2])
            elif argv[1] == 'image':
                return Image(argv[2])
            elif argv[1] == 'video':
                return Video(argv[2])
            elif argv[1] == 'image2':
                return Image2(argv[2])
            elif argv[1] == 'video2':
                return Video2(argv[2])
        except Exception as err:
            self.logger.info('인자를 올바르게 입력하세요')
            sys.exit()


if __name__ == '__main__':
    '''
    python main.py http dlwlrma
    python main.py user dlwlrma
    python main.py post dlwlrma
    python main.py file dlwlrma
    python main.py image dlwlrma
    python main.py image2 dlwlrma
    python main.py video dlwlrma
    '''
    mylogger = createLogger('Main')

    mylogger.info('Main start')
    instaFactory = InstaFactory(mylogger)
    insta = instaFactory.create(sys.argv)
    insta.run()
    mylogger.info('Main end')
