from Util import Util
import sys
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint


def getFilesInner(item):
    result = DotMap()
    if 'image_versions2' in item:
        result.image = item.image_versions2.candidates[0].url
    if 'video_versions' in item:
        result.video = item.video_versions[0].url
    return result


def getFiles(item):
    if 'carousel_media' not in item:
        return [getFilesInner(item)]

    result = []
    for carousel_item in item.carousel_media:
        result.append(getFilesInner(carousel_item))
    return result


if __name__ == '__main__':
    util = Util()
    data = util.readFile('20230517023027858504.json')
    data = DotMap(json.loads(data))

    apple = DotMap()
    data.fitems = data.pop('items')
    apple.user = data.user

    apple.posts = []
    pprint(len(data.fitems))
    for item in data.fitems:
        itemTemp = DotMap()
        itemTemp.taken_at = item.taken_at
        itemTemp.pk = item.pk
        itemTemp.id = item.id
        itemTemp.media_type = item.media_type
        itemTemp.code = item.code
        itemTemp.carousel_media_count = item.carousel_media_count if 'carousel_media_count' in item else 1
        itemTemp.comment_count = item.comment_count

        if item.caption:
            itemTemp.text = item.caption.text
            itemTemp.status = item.caption.status
            itemTemp.created_at = item.caption.created_at
        else:
            itemTemp.text = ''
            itemTemp.status = ''
            itemTemp.created_at = ''

        itemTemp.files = getFiles(item)
        apple.posts.append(itemTemp)

    pprint(apple.posts[0])
    # pprint(apple.posts)
    util.saveFile(f'{util.now()}_aa.json', json.dumps(apple.toDict()))
