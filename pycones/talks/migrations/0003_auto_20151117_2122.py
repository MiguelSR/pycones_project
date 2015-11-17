# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0002_auto_20151116_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='description',
            field=models.TextField(),
        ),
    ]
