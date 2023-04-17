from django.contrib.auth.models import User as DjangoUser
from django.db import models
from django.utils import timezone
import datetime
import uuid

class User(models.Model):
    seq = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pks = models.CharField(max_length=255,null=True)
    pks_id = models.CharField(max_length=255,null=True)
    username = models.CharField(max_length=255,null=True)
    full_name = models.CharField(max_length=255,null=True)
    is_private = models.BooleanField(default=False,null=True)
    is_verified = models.BooleanField(default=False,null=True)
    profile_key = models.CharField(max_length=255,null=True)
    profile_pic_id = models.CharField(max_length=255,null=True)
    profile_pic_url = models.TextField(null=True)
    profile_grid_display_type = models.CharField(max_length=255,null=True)
    updated_at = models.DateTimeField(default=timezone.now,null=True)
    created_at = models.DateTimeField(default=timezone.now,null=True)

# class Post(models.Model):
#     seq = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     mode = models.CharField(default='post',max_length=255,null=True)
#     id = models.CharField(max_length=255,null=True)
#     id_num = models.CharField(max_length=255,null=True)
#     state = models.IntegerField(default=0,null=True)
#     content = models.TextField(null=True)
#     # tags = jsonfield.JSONField(null=True)
#     orders = models.IntegerField(null=True)
#     uploaded = models.DateTimeField(null=True)
#     file_cnt = models.IntegerField(default=0,null=True)
#     is_restricted = models.BooleanField(default=False,null=True)
#     created = models.DateTimeField(default=timezone.now,null=True)
#     user_id = models.CharField(max_length=255,null=True)
#     tag_id = models.CharField(max_length=255,null=True)

# class User(models.Model):
#     seq = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     mode = models.CharField(default='user',max_length=255,null=True)
#     id = models.CharField(max_length=255,null=True)
#     id_num = models.CharField(max_length=255,null=True)
#     state = models.IntegerField(default=0,null=True)
#     name = models.CharField(max_length=255,null=True)
#     biography = models.TextField(null=True)
#     followers = models.IntegerField(null=True)
#     following = models.IntegerField(null=True)
#     profile_url = models.CharField(max_length=1023,null=True)
#     profile_key = models.CharField(max_length=255,null=True)
#     profile_fullfname = models.CharField(max_length=255,null=True)
#     file_cnt = models.IntegerField(default=0,null=True)
#     post_cnt = models.IntegerField(default=0,null=True)
#     post_cnt_str = models.CharField(max_length=255,null=True)
#     latest_post_id = models.CharField(max_length=255,null=True)
#     is_private = models.BooleanField(default=False,null=True)
#     is_restricted = models.BooleanField(default=False,null=True)
#     dates = models.DateField(default=datetime.date.today,null=True)
#     created_at = models.DateTimeField(default=timezone.now,null=True)