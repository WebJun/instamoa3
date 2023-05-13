import sys
import os

sys.dont_write_bytecode = True
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoOrm.settings")
import django

django.setup()
from django.db.models import Q, Max, Min
from djangoOrm.insta.models import (
    User,
    Post,
    File,
)
from dotmap import DotMap  # pip install dotmap

class Model:

    def getUsers(self, seq):
        return User.objects.filter(seq=seq).values()

    def saveUser(self, userId, user):
        # pprint(user)
        userSet = User()
        userSet.user_id = userId
        userSet.kkk = user.toDict()
        userSet.save()

    def savePosts(self, userId, postIds, posts):
        for index, post in enumerate(posts):
            postSet = Post()
            postSet.user_id = userId
            postSet.post_id = postIds[index]
            postSet.kkk = post.toDict()
            postSet.save()

    def saveFiles(self, userId, files):
        posts = files
        for index, post in enumerate(posts):
            for index, file in enumerate(post.files):
                fileSet = File()
                fileSet.user_id = userId
                fileSet.post_id = post.code
                fileSet.kkk = file
                fileSet.save()
