from Util import Util
import json
from pprint import pprint
from dotmap import DotMap  # pip install dotmap
import sys
from Model import Model
import requests

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
        
    model.saveUser(apple.user)
    model.savePosts(apple.posts)    
    model.saveFiles(apple.userId, apple.files)
    
    
    
    user_id = apple.user.pks
    qq = len(apple.posts)
    max_id = apple.posts[qq-1].id
        
    headers = {
        'X-IG-App-ID': '936619743392459',
    }
    params = {
        'count': '12',
        'max_id': max_id,
    }
    now = util.now()
    response = requests.get(
        f'https://www.instagram.com/api/v1/feed/user/{user_id}/',
        params=params,
        headers=headers,
    )
    util = Util()
    util.saveFile(f'{now}.json', response.text)