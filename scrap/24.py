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
        # print(99)
        itemTemp = DotMap()

        itemTemp.taken_at = item.taken_at
        itemTemp.pk = item.pk
        itemTemp.id = item.id
        itemTemp.media_type = item.media_type
        itemTemp.code = item.code
        itemTemp.carousel_media_count = item.carousel_media_count if 'carousel_media_count' in item else 1

        # 여러개인 경우
        if 'carousel_media' in item:
            print(1, itemTemp.code)

        # 파일이 1개인 경우
        elif 'image_versions2' in item:
            print(12, itemTemp.code)
        else:
            pprint('에러')

        apple.posts.append(itemTemp)

    pprint(apple.posts[0])
    # pprint(apple.posts)
    util.saveFile(f'{util.now()}_aa.json', json.dumps(apple.toDict()))
