# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20160920_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='track_length',
            field=models.TimeField(),
        ),
    ]
