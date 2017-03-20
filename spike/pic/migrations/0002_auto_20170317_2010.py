# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='gif',
            field=models.ImageField(upload_to=b'submission_uploads/gifs/'),
        ),
    ]
