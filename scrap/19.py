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
    # pprint(user.caption)
    # pprint(user.user)
    # pprint(user.items)
    
    # key중에 items이 items() 메소드와 겹치는 문제
    user.iitems = user.pop('items')
    
    posts = [item.caption for item in user.iitems]
    postIds = [item.code for item in user.iitems]
    
    pprint(postIds)
    

    model.saveUser(userId, user.user)
    model.savePosts(userId, postIds, posts)
    # model.saveUser(userId, post.user)
