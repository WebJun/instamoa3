from Util import Util
import sys
import json
from dotmap import DotMap  # pip install dotmap
from pprint import pprint

if __name__ == '__main__':
    util = Util()
    data = util.readFile('20230517023027858504.json')
    data = DotMap(json.loads(data))

    apple = DotMap()
    data.fitems = data.pop('items')
    apple.user = data.user

    # user
    # pprint(apple.user)

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

        itemTemp.files = []

        sss = DotMap()
        # 파일이 1개인 경우
        if 'image_versions2' in item:
            sss.image = item.image_versions2.candidates[0].url
        if 'video_versions' in item:
            sss.video = item.video_versions[0].url
        if 'image_versions2' in item or 'video_versions' in item:
            itemTemp.files.append(sss)

        # 파일이 여러개인 경우
        if 'carousel_media' in item:
            for qqq in item.carousel_media:
                sss = DotMap()
                if 'image_versions2' in qqq:
                    sss.image = qqq.image_versions2.candidates[0].url
                if 'video_versions' in qqq:
                    sss.video = qqq.video_versions[0].url
                if 'image_versions2' in qqq or 'video_versions' in qqq:
                    itemTemp.files.append(sss)
        apple.posts.append(itemTemp)

    pprint(apple.posts[0])
    # pprint(apple.posts)
    util.saveFile(f'{util.now()}_aa.json', json.dumps(apple.toDict()))
