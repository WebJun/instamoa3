# Generated by Django 3.2 on 2021-05-01 22:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QueueModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ids', models.CharField(max_length=255, null=True)),
                ('mode', models.CharField(max_length=255, null=True)),
                ('a0100_stime', models.CharField(max_length=255, null=True)),
                ('a0100_etime', models.CharField(max_length=255, null=True)),
                ('a0200_stime', models.CharField(max_length=255, null=True)),
                ('a0200_etime', models.CharField(max_length=255, null=True)),
                ('a0300_stime', models.CharField(max_length=255, null=True)),
                ('a0300_etime', models.CharField(max_length=255, null=True)),
                ('a0400_stime', models.CharField(max_length=255, null=True)),
                ('a0400_etime', models.CharField(max_length=255, null=True)),
                ('a0500_stime', models.CharField(max_length=255, null=True)),
                ('a0500_etime', models.CharField(max_length=255, null=True)),
                ('b0100_stime', models.CharField(max_length=255, null=True)),
                ('b0100_etime', models.CharField(max_length=255, null=True)),
                ('state', models.IntegerField(default=0, null=True)),
                ('ip', models.CharField(max_length=255, null=True)),
                ('is_use', models.IntegerField(default=1, null=True)),
                ('dates', models.DateField(default=datetime.date.today, null=True)),
                ('modified', models.DateTimeField(null=True)),
                ('created', models.DateTimeField(null=True)),
            ],
        ),
    ]
