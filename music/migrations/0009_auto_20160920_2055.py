# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20160920_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='wiki_url',
            field=models.URLField(blank=True),
        ),
    ]
