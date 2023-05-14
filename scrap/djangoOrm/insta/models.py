from django.contrib.auth.models import User as DjangoUser
from django.db import models
from django.utils import timezone
import datetime
import uuid
import jsonfield  # pip install django-jsonfield
import json


class User(models.Model):
    seq = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    pks = models.CharField(max_length=255, null=True)
    pks_id = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=255, null=True)
    is_private = models.CharField(max_length=255, null=True)


class Post(models.Model):
    seq = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, null=True)
    media_type = models.CharField(max_length=255, null=True)
    pks = models.CharField(max_length=255, null=True)
    id = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=255, null=True)
    created_at = models.CharField(max_length=255, null=True)
    text = models.TextField(null=True)
    media_id = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)


class File(models.Model):
    seq = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=255, null=True)
    url = models.TextField(null=True)
    media_type = models.CharField(max_length=255, null=True)
