from pprint import pprint
from dotmap import DotMap  # pip install dotmap
from djangoOrm.insta.models import (
    User,
)
from django.db.models import Q, Max, Min
import django
import sys
import os
sys.dont_write_bytecode = True
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoOrm.settings")

django.setup()


class Model:

    def getUsers(self, seq):
        return User.objects.filter(seq=seq).values()

    def saveUser(self, user):
        user.pks = user.pop("pk")
        user.pks_id = user.pop("pk_id")

        userSet = User(**user)
        userSet.save()

    def saveFiles(self, posts):

        pprint(posts[0])

        value = []
        for file in self.files:
            apple = {
                'user_id': file['user_id'],
                'post_id': file['post_id'],
                'tag_id': file['tag_id'],
                'orders': file['order'],
                'cdn': file['cdn'],
                'img_url': file['img_url'],
                'img_key': file['img_key'],
                'img_fullfname': file['img_fullfname'],
                'caption': file['caption'],
                'is_video': file['is_video'],
                'video_url': file['video_url'],
                'video_key': file['video_key'],
                'video_fullfname': file['video_fullfname'],
                'uploaded': file['uploaded'],
                'post_seq': file['post_seq'],
            }
            if self.mode == 'user':
                apple['user_seq'] = file['user_seq']
            elif self.mode == 'tag':
                apple['tag_seq'] = file['tag_seq']
            value.append(
                File(**apple)
            )
        File.objects.bulk_create(value)

    def saveUser2(self, user):
        user.pks = user.pop("pk")
        user.pks_id = user.pop("pk_id")

        userSet = User(**user)
        userSet.save()
