from django.contrib.auth.models import User as DjangoUser
from django.db import models
from django.utils import timezone
import datetime
import jsonfield # pip install django-jsonfield
import json
import uuid

class User(models.Model):
    seq = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mode = models.CharField(default='user',max_length=255,null=True)
    id = models.CharField(max_length=255,null=True)
    id_num = models.CharField(max_length=255,null=True)
    state = models.IntegerField(default=0,null=True)
    name = models.CharField(max_length=255,null=True)
    biography = models.TextField(null=True)
    followers = models.CharField(max_length=255,null=True)
    following = models.CharField(max_length=255,null=True)
    profile_url = models.CharField(max_length=1023,null=True)
    profile_key = models.CharField(max_length=255,null=True)
    profile_fullfname = models.CharField(max_length=255,null=True)
    file_cnt = models.IntegerField(default=0,null=True)
    post_cnt = models.IntegerField(default=0,null=True)
    post_cnt_str = models.CharField(max_length=255,null=True)
    latest_post_id = models.CharField(max_length=255,null=True)
    is_private = models.BooleanField(default=False,null=True)
    is_restricted = models.BooleanField(default=False,null=True)
    dates = models.DateField(default=datetime.date.today,null=True)
    created = models.DateTimeField(default=timezone.now,null=True)

class Post(models.Model):
    seq = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mode = models.CharField(default='post',max_length=255,null=True)
    id = models.CharField(max_length=255,null=True)
    id_num = models.CharField(max_length=255,null=True)
    state = models.IntegerField(default=0,null=True)
    content = models.TextField(null=True)
    tags = jsonfield.JSONField(null=True)
    orders = models.IntegerField(null=True)
    uploaded = models.DateTimeField(null=True)
    file_cnt = models.IntegerField(default=0,null=True)
    is_restricted = models.BooleanField(default=False,null=True)
    created = models.DateTimeField(default=timezone.now,null=True)
    user_id = models.CharField(max_length=255,null=True)

class File(models.Model):
    seq = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_video = models.BooleanField(default=False,null=True)
    img_url = models.CharField(max_length=1023,null=True)
    img_fullfname = models.CharField(max_length=255,null=True)
    img_key = models.CharField(max_length=255,null=True)
    img_state = models.IntegerField(default=0,null=True)
    video_url = models.CharField(max_length=1023,null=True)
    video_fullfname = models.CharField(max_length=255,null=True)
    video_key = models.CharField(max_length=255,null=True)
    video_state = models.IntegerField(default=0,null=True)
    post_orders = models.IntegerField(null=True)
    orders = models.IntegerField(null=True)
    cdn = models.CharField(default='cdn2',max_length=255,null=True)
    caption = models.TextField(null=True)
    created = models.DateTimeField(default=timezone.now,null=True)
    uploaded = models.DateTimeField(default=timezone.now,null=True) # TODO::default 없어야함
    user_id = models.CharField(max_length=255,null=True)
    tag_id = models.CharField(max_length=255,null=True)
    post_id = models.CharField(max_length=255,null=True)