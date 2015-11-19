# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0004_auto_20151119_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='authors',
            field=models.ManyToManyField(related_name='talks', null=True, to='authors.Author', blank=True),
        ),
    ]
