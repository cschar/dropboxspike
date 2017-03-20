# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0002_auto_20170317_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='scene',
            field=models.ForeignKey(to='pic.Scene', null=True),
        ),
    ]
