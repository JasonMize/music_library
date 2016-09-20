# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20160920_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('audio_format', models.CharField(default='Digital', max_length=40, choices=[('Vinyl', 'Vinyl'), ('Compact Disc', 'Compact Disc'), ('Digital', 'Digital'), ('Phonograph Cylinder', 'Phonograph Cylinder')])),
                ('year', models.IntegerField()),
                ('genre', models.CharField(default="Rock 'n Roll", max_length=40, choices=[("Rock 'n Roll", "Rock 'n Roll"), ('Punk', 'Punk')])),
                ('collection', models.BooleanField(default=False)),
                ('owned', models.BooleanField(default=False)),
                ('artists', models.ManyToManyField(to='music.Artist')),
            ],
        ),
        migrations.RemoveField(
            model_name='albums',
            name='artist',
        ),
        migrations.DeleteModel(
            name='Albums',
        ),
    ]
