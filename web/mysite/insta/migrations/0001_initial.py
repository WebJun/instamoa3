# Generated by Django 4.0.3 on 2023-04-16 22:58

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('seq', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pks', models.CharField(max_length=255, null=True)),
                ('pks_id', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=255, null=True)),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('is_private', models.BooleanField(default=False, null=True)),
                ('is_verified', models.BooleanField(default=False, null=True)),
                ('profile_key', models.CharField(max_length=255, null=True)),
                ('profile_pic_id', models.CharField(max_length=255, null=True)),
                ('profile_pic_url', models.TextField(null=True)),
                ('profile_grid_display_type', models.CharField(max_length=255, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
