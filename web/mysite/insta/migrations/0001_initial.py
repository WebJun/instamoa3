# Generated by Django 3.2.17 on 2023-05-01 17:16

from django.db import migrations, models
import django.utils.timezone
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('seq', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=255, null=True)),
                ('post_id', models.CharField(max_length=255, null=True)),
                ('is_video', models.BooleanField(default=False, null=True)),
                ('img_url', models.CharField(max_length=1023, null=True)),
                ('img_fullfname', models.CharField(max_length=255, null=True)),
                ('img_key', models.CharField(max_length=255, null=True)),
                ('img_state', models.IntegerField(default=0, null=True)),
                ('video_url', models.CharField(max_length=1023, null=True)),
                ('video_fullfname', models.CharField(max_length=255, null=True)),
                ('video_key', models.CharField(max_length=255, null=True)),
                ('video_state', models.IntegerField(default=0, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('uploaded', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('seq', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=255, null=True)),
                ('post_id', models.CharField(max_length=255, null=True)),
                ('file_id', models.CharField(max_length=255, null=True)),
                ('kkk', jsonfield.fields.JSONField(null=True)),
            ],
        ),
    ]
