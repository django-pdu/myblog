# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reason',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
