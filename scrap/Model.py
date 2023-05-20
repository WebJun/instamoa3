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

    username = ''

    def getUsers(self):
        return User.objects.filter(username=self.username).values()

    def getPosts(self):
        return Post.objects.filter(username=self.username).values()

    def getFiles(self):
        return File.objects.filter(username=self.username).values()

    def saveUser(self, user):
        user.pks = user.pop("pk")
        user.pks_id = user.pop("pk_id")
        user = self.filterExistField(user, User)
        userSet = User(**user)
        userSet.save()

    def savePosts(self, posts):
        postArr = []
        for post in posts:
            post.pks = post.pop("pk")
            post = self.filterExistField(post, Post)
            postArr.append(Post(**post))
        Post.objects.bulk_create(postArr)

    def saveFiles(self, files):
        fileArr = []
        for file in files:
            file = self.filterExistField(file, File)
            fileArr.append(File(**file))
        File.objects.bulk_create(fileArr)

    def filterExistField(self, user, Table):
        lst1 = [field.name for field in Table._meta.get_fields()]
        lst2 = user.keys()
        intersection = list(set(lst1) & set(lst2))
        return {k: v for k, v in user.items() if k in intersection}
