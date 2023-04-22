import sys
import os

sys.dont_write_bytecode = True
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoOrm.settings")
import django

django.setup()
from django.db.models import Q, Max, Min
from djangoOrm.insta.models import (
    User,
)
from dotmap import DotMap  # pip install dotmap

class Model:

    def getUsers(self, seq):
        return User.objects.filter(seq=seq).values()

    def saveUser(self, user):
        user.pks = user.pk
        user.pks_id = user.pk_id

        userSet = User()
        userSet.pks = user.pks
        userSet.pks_id = user.pks_id
        userSet.username = user.username
        userSet.full_name = user.full_name
        userSet.is_private = user.is_private
        userSet.is_verified = user.is_verified
        # userSet.profile_key = user.profile_key
        print(isinstance(user.profile_pic_id, 'dotmap.DotMap'))
        print(isinstance(user.profile_pic_idaa, 'dotmap.DotMap'))
        # if user.profile_pic_id is not None:
            # userSet.profile_pic_id = user.profile_pic_id 
        userSet.profile_pic_url = user.profile_pic_url
        userSet.profile_grid_display_type = user.profile_grid_display_type
        userSet.save()

    # def saveUser(self, user):
    #     user.pks = user.pk
    #     user.pks_id = user.pk_id

    #     userSet = User()
    #     userSet.pks = user.pks
    #     userSet.pks_id = user.pks_id
    #     userSet.username = user.username
    #     userSet.full_name = user.full_name
    #     userSet.is_private = user.is_private
    #     userSet.is_verified = user.is_verified
    #     # userSet.profile_key = user.profile_key
    #     # userSet.profile_pic_id = user.profile_pic_id
    #     userSet.profile_pic_url = user.profile_pic_url
    #     userSet.profile_grid_display_type = user.profile_grid_display_type
    #     userSet.save()
