import sys
from Http import Http
# from User import User
# from Post import Post
# from File import File
# from Copy import Copy
import logging
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
            # elif argv[1] == 'user':
            #     return User(argv[2])
            # elif argv[1] == 'post':
            #     return Post(argv[2])
            # elif argv[1] == 'file':
            #     return File(argv[2])
            # elif argv[1] == 'copy':
            #     return Copy(argv[2])
        except Exception as err:
            self.logger.info('인자를 올바르게 입력하세요')
            sys.exit()


if __name__ == '__main__':
    '''
    python main.py http okjayeon
    python main.py user okjayeon
    python main.py post okjayeon
    python main.py file okjayeon    
    '''
    mylogger = createLogger('Main')

    mylogger.info('Main start')
    instaFactory = InstaFactory(mylogger)
    insta = instaFactory.create(sys.argv)
    insta.run()
    mylogger.info('Main end')
