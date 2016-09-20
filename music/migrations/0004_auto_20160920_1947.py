# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_albums'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='year',
            field=models.IntegerField(),
        ),
    ]
