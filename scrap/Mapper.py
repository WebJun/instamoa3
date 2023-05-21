
from dotmap import DotMap  # pip install dotmap
from datetime import datetime
from Util import Util


class Mapper:

    username = ''
    taken_at = ''

    def __init__(self):
        self.util = Util()

    def getFiles(self, item):
        code = item.code
        taken_at = item.taken_at
        if 'carousel_media' not in item:
            return [self.getFilesInner(item, code, taken_at, 1)]

        result = []
        for index, carousel_item in enumerate(item.carousel_media, start=1):
            result.append(self.getFilesInner(
                carousel_item, code, taken_at, index))
        return result

    def getFilesInner(self, item, code, taken_at, index):
        result = DotMap()
        result.username = self.username
        result.code = code
        result.taken_at = taken_at
        result.id = item.id
        result.image = None
        result.video = None
        if 'image_versions2' in item:
            result.image = item.image_versions2.candidates[0].url
        if 'video_versions' in item:
            result.video = item.video_versions[0].url
        result = self.getLocalname(result, index)
        return result

    def getLocalname(self, res, index):
        apple = datetime.fromtimestamp(int(res.taken_at))
        cdn = 'cdn3'
        if res.image != None:
            res.image_local = f"{apple.strftime('%Y%m%d%H%M%S')}+{cdn}+{res.username}+{res.code}+{self.util.zfill3(index)}.jpg"
        if res.video != None:
            res.video_local = f"{apple.strftime('%Y%m%d%H%M%S')}+{cdn}+{res.username}+{res.code}+{self.util.zfill3(index)}.mp4"
        return res

    def getPosts(self, item):
        itemTemp = DotMap()
        itemTemp.username = self.username
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
        return itemTemp
