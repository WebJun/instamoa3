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
        user = self.filterExistField(user, User)
        userSet = User(**user)
        userSet.save()

    def savePosts(self, username, posts):
        postArr = []
        for post in posts:
            post.pks = post.pop("pk")
            post.pks_id = post.pop("pk_id")
            post.username = username
            post = self.filterExistField(post, Post)
            postArr.append(Post(**post))
        Post.objects.bulk_create(postArr)

    def saveFiles(self, username, files):
        posts = files
        fileArr = []
        for index, post in enumerate(posts):
            for index, file in enumerate(post.files):
                fileSet = File()
                fileSet.username = username
                fileSet.code = post.code
                fileSet.url = file
                fileArr.append(fileSet)
        File.objects.bulk_create(fileArr)

    def getFiles(self):
        return File.objects.values()

    def filterExistField(self, user, Table):
        lst1 = [field.name for field in Table._meta.get_fields()]
        lst2 = user.keys()
        intersection = list(set(lst1) & set(lst2))
        return {k: v for k, v in user.items() if k in intersection}
