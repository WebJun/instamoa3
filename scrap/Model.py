from pprint import pprint
from dotmap import DotMap  # pip install dotmap
from djangoOrm import orm
from djangoOrm.insta.models import (
    User,
    Post,
    File,
    Process
)
from django.db.models import Q, Max, Min


class Model:

    username = ''

    def getProcess(self):
        return Process.objects.values()

    def getUsers(self):
        return User.objects.filter(username=self.username).values()

    def getPosts(self):
        return Post.objects.filter(username=self.username).values()

    def getFiles(self):
        return File.objects.filter(username=self.username).values()
        # return File.objects.filter(username=self.username, image_status__isnull=True).values()

    def savePorcess(self, data):
        userSet = Process(**data)
        userSet.save()

    def updatePorcess(self, pid):
        Process.objects.filter(pid=pid).update(status=200)

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

    def updateImageFiles(self, files):
        fileSeqs = [file.seq for file in files if file.image_status == 200]
        if fileSeqs:
            File.objects.filter(seq__in=fileSeqs).update(image_status=200)

        fileSeqs = [file.seq for file in files if file.image_status == 400]
        if fileSeqs:
            File.objects.filter(seq__in=fileSeqs).update(image_status=400)

    def updateVideoFiles(self, files):
        fileSeqs = [file.seq for file in files if file.video_status == 200]
        if fileSeqs:
            File.objects.filter(seq__in=fileSeqs).update(video_status=200)

        fileSeqs = [file.seq for file in files if file.video_status == 400]
        if fileSeqs:
            File.objects.filter(seq__in=fileSeqs).update(video_status=400)

    def filterExistField(self, user, Table):
        lst1 = [field.name for field in Table._meta.get_fields()]
        lst2 = user.keys()
        intersection = list(set(lst1) & set(lst2))
        return {k: v for k, v in user.items() if k in intersection}
