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
    # user.iitems = user.pop('items')
    # posts = [item for item in user.iitems]
    # postIds = [post.code for post in posts]
    
    # files = [post.image_versions2 for post in posts]
    # pprint(files)
    
    # pprint(postIds)

    # model.saveUser(userId, user.user)
    # model.savePosts(userId, postIds, posts)
    # model.saveUser(userId, post.user)
    user.fitems = user.pop('items')

    apple = DotMap()
    # apple.user = user.user

    def inner(media):
        return [v.url for i,v in enumerate(media.image_versions2.candidates) if i==0]

    def outer(item):
        return [inner(media) for media in item.carousel_media] if 'carousel_media' in item else inner(item)

    apple.posts = [DotMap({'code':item.code,'files':outer(item)}) for item in user.fitems]
    pprint(apple)