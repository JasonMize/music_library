# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='solo_vs_band',
            field=models.CharField(max_length=40, choices=[('Solo Artist', 'Solo Artist'), ('Band', 'Band')], default='Solo Artist'),
        ),
    ]
