# Generated by Django 3.2.17 on 2023-05-13 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20230513_0730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_id',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='file_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='pks',
        ),
        migrations.RemoveField(
            model_name='post',
            name='kkk',
        ),
        migrations.RemoveField(
            model_name='user',
            name='file_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='kkk',
        ),
        migrations.RemoveField(
            model_name='user',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
    ]