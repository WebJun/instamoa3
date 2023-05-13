from Util import Util
import json
from pprint import pprint
from dotmap import DotMap  # pip install dotmap
import sys
from Model import Model

if __name__ == '__main__':
    util = Util()
    model = Model()

    apple = DotMap()
    apple.userId = 'dlwlrma'

    user = util.readFile('20230425230210092209.json')
    user = json.loads(user)
    user = DotMap(user)
    user.fitems = user.pop('items')
    
    apple.user = user.user

    apple.posts = [DotMap({ **item.caption, **item}) for item in user.fitems]
    apple.postIds = [item.code for item in user.fitems]
    
    def inner(media):
        a = [v.url for i,v in enumerate(media.image_versions2.candidates) if i==0]
        return a

    def outer(item):
        return [inner(media)[0] for media in item.carousel_media] if 'carousel_media' in item else inner(item)

    apple.files = [DotMap({'code':item.code,'files':outer(item)}) for item in user.fitems]
        
    model.saveUser(apple.userId, apple.user)
    model.savePosts(apple.userId, apple.postIds, apple.posts)    
    model.saveFiles(apple.userId, apple.files)
