from Util import Util
import json
from pprint import pprint
from dotmap import DotMap  # pip install dotmap
import sys
from Model import Model

if __name__ == '__main__':
    util = Util()
    model = Model()

    userId = 'dlwlrma'

    post = util.readFile('1.json')
    post = json.loads(post)
    post = DotMap(post)

    # pprint(post.carousel_media)
    # pprint(post.caption)
    pprint(post.user)
    
    model.saveUser(userId, post.user)
    model.savePosts(userId, post.caption)
    # model.saveUser(userId, post.user)
