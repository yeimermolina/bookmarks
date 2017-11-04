# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_user_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='total_likes',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
