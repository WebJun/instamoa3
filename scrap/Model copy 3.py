from pprint import pprint
import json
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

    def saveUser(self, userId, user):
        # pprint(user)
        userSet = User()
        userSet.user_id = userId
        userSet.kkk = dict(user)
        userSet.save()

    def savePosts(self, userId, user):
        pass

    # def saveUser(self, user):
    #     user.pks = user.pop("pk")
    #     user.pks_id = user.pop("pk_id")

    #     userSet = User(**user)
    #     userSet.save()
