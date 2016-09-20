# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20160920_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('track_number', models.IntegerField()),
                ('track_length', models.IntegerField()),
                ('album', models.ForeignKey(to='music.Album')),
            ],
        ),
        migrations.AddField(
            model_name='composer',
            name='songs',
            field=models.ManyToManyField(to='music.Song'),
        ),
    ]
