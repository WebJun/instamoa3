from pprint import pprint
from dotmap import DotMap  # pip install dotmap
from djangoOrm import orm
from djangoOrm.insta.models import (
    User,
    Post,
    File,
)
from django.db.models import Q, Max, Min


class Model:

    def getUsers(self, seq):
        return User.objects.filter(seq=seq).values()

    def saveUser(self, user):
        user.pks = user.pop("pk")
        user.pks_id = user.pop("pk_id")
        user = self.filter(user, User)
        userSet = User(**user)
        userSet.save()

    def filter(self, user, Table):
        lst1 = [field.name for field in Table._meta.get_fields()]
        lst2 = user.keys()
        intersection = list(set(lst1) & set(lst2))
        return {k: v for k, v in user.items() if k in intersection}

    def savePosts(self, username, posts):
        for post in posts:
            post.pks = post.pop("pk")
            post.pks_id = post.pop("pk_id")
            post.username = username
            post = self.filter(post, Post)
            postSet = Post(**post)
            postSet.save()

    def saveFiles(self, username, files):
        posts = files
        for index, post in enumerate(posts):
            for index, file in enumerate(post.files):
                fileSet = File()
                fileSet.username = username
                fileSet.code = post.code
                fileSet.url = file
                fileSet.save()
