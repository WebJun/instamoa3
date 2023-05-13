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

    user = util.readFile('20230425230210092209.json')
    user = json.loads(user)
    user = DotMap(user)

    # pprint(post.carousel_media)
    # pprint(post.caption)
    pprint(user.user)
    
    model.saveUser(userId, user.user)
    # model.savePosts(userId, user.caption)
    # model.saveUser(userId, post.user)
