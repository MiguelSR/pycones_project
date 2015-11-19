# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0003_auto_20151117_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='authors',
            field=models.ManyToManyField(related_name='talks', to='authors.Author'),
        ),
    ]
