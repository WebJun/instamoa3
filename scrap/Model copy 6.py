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
from pprint import pprint

class Model:

    def getUsers(self, seq):
        return User.objects.filter(seq=seq).values()

    def saveUser(self, userId, user):        
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
    
    def savePosts(self, userId, postIds, posts):
        # pprint(posts)
        for index, post in enumerate(posts):
            post.pks = post.pop("pk")
            post.pks_id = post.pop("pk_id")
            post = self.filter(post, Post)
            pprint(post)
            postSet = Post(**post)
            postSet.save()
        # for index, post in enumerate(posts):
        #     postSet = Post()
        #     postSet.user_id = userId
        #     postSet.post_id = postIds[index]
        #     postSet.kkk = post.toDict()
        #     postSet.save()

    def saveFiles(self, userId, files):
        posts = files
        for index, post in enumerate(posts):
            for index, file in enumerate(post.files):
                fileSet = File()
                fileSet.user_id = userId
                fileSet.post_id = post.code
                fileSet.kkk = file
                fileSet.save()
