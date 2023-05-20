from Util import Util
import sys
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint


def getFilesInner(item, username, code):
    result = DotMap()
    result.username = username
    result.code = code
    if 'image_versions2' in item:
        result.image = item.image_versions2.candidates[0].url
    if 'video_versions' in item:
        result.video = item.video_versions[0].url
    return result


def getFiles(item):
    username = item.user.username
    code = item.code
    if 'carousel_media' not in item:
        return [getFilesInner(item, username, code)]

    result = []
    for carousel_item in item.carousel_media:
        result.append(getFilesInner(carousel_item, username, code))
    return result


def getPosts(item):
    itemTemp = DotMap()
    itemTemp.taken_at = item.taken_at
    itemTemp.pk = item.pk
    itemTemp.id = item.id
    itemTemp.media_type = item.media_type
    itemTemp.code = item.code
    itemTemp.carousel_media_count = item.carousel_media_count if 'carousel_media_count' in item else 1
    itemTemp.comment_count = item.comment_count
    itemTemp.username = item.user.username

    if item.caption:
        itemTemp.text = item.caption.text
        itemTemp.status = item.caption.status
        itemTemp.created_at = item.caption.created_at
    else:
        itemTemp.text = ''
        itemTemp.status = ''
        itemTemp.created_at = ''
    return itemTemp


if __name__ == '__main__':
    util = Util()
    data = util.readFile('20230517023027858504.json')
    data = DotMap(json.loads(data))

    apple = DotMap()
    data.fitems = data.pop('items')
    apple.user = data.user

    apple.posts = []
    for item in data.fitems:
        apple.posts.append(getPosts(item))

    apple.files = []
    for item in data.fitems:
        apple.files = apple.files + getFiles(item)

    util.saveFile(f'{util.now()}_aa.json', json.dumps(apple.toDict()))