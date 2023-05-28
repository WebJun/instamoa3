import sys
from All import All
from Http import Http
from Http2 import Http2
from User import User
from Post import Post
from File import File
from Image import Image
from Image2 import Image2
from Image3 import Image3
from Video import Video
from Video2 import Video2
from Video3 import Video3
import json
from createLogger import createLogger


class InstaFactory:

    logger = None

    def __init__(self, logger):
        self.logger = logger

    def create(self, argv):
        self.logger.info(json.dumps(argv))
        try:
            if argv[1] == 'all':
                return All(argv[2])
            elif argv[1] == 'http':
                return Http(argv[2])
            elif argv[1] == 'http2':
                return Http2(argv[2])
            elif argv[1] == 'user':
                return User(argv[2])
            elif argv[1] == 'post':
                return Post(argv[2])
            elif argv[1] == 'file':
                return File(argv[2])
            elif argv[1] == 'image':
                return Image(argv[2])
            elif argv[1] == 'image2':
                return Image2(argv[2])
            elif argv[1] == 'image3':
                return Image3(argv[2])
            elif argv[1] == 'video':
                return Video(argv[2])
            elif argv[1] == 'video2':
                return Video2(argv[2])
            elif argv[1] == 'video3':
                return Video3(argv[2])
        except Exception as err:
            self.logger.info('인자를 올바르게 입력하세요')
            sys.exit()


if __name__ == '__main__':
    '''
    python main.py all kimviju
    python main.py one kimviju
    python main.py two kimviju

    python main.py http kimviju
    python main.py http2 kimviju

    python main.py user kimviju
    python main.py post kimviju
    python main.py file kimviju
    python main.py image kimviju
    python main.py image2 kimviju
    python main.py image3 kimviju
    python main.py video kimviju
    python main.py video2 kimviju
    python main.py video3 kimviju
    '''
    mylogger = createLogger('Main')

    mylogger.info('Main start')
    instaFactory = InstaFactory(mylogger)
    insta = instaFactory.create(sys.argv)
    insta.run()
    mylogger.info('Main end')
