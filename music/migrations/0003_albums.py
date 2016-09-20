# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_artist_solo_vs_band'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('audio_format', models.CharField(max_length=40, choices=[('Vinyl', 'Vinyl'), ('Compact Disc', 'Compact Disc'), ('Digital', 'Digital'), ('Phonograph Cylinder', 'Phonograph Cylinder')], default='Digital')),
                ('year', models.IntegerField(max_length=4)),
                ('genre', models.CharField(max_length=40, choices=[("Rock 'n Roll", "Rock 'n Roll"), ('Punk', 'Punk')], default="Rock 'n Roll")),
                ('collection', models.BooleanField(default=False)),
                ('artist', models.ManyToManyField(to='music.Artist')),
            ],
        ),
    ]
