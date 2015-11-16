# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def create_talks(apps, schema_director):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Author = apps.get_model('authors', 'Author')
    Talk = apps.get_model('talks', 'Talk')

    miguel_sanchez = Author(name='Miguel Sanchez', python_level=1)
    miguel_sanchez.save()

    miguel_gonzalez = Author(name='Miguel Gonzalez', python_level=42)
    miguel_gonzalez.save()

    backbone_talk = Talk(name='SPAs con Django y Backbone',
                         description='En este taller llevaremos a cabo un caso práctico. La construcción de una Single-Page Application usando Backbone como herramienta front-end. Ahora que cada día aparece una docena de frameworks de JavaScript, suena sensato buscar algo de estabilidad en un framework de trayectoria ya constatada, como es Backbone. Por otra parte, tener un framework como Django en el back-end proporciona robustez, facilidad de uso y muchísima extensibilidad -gracias al increíble ecosistema pythónico-.')
    backbone_talk.save()
    backbone_talk.authors.add(miguel_sanchez)
    backbone_talk.authors.add(miguel_gonzalez)

class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0001_initial'),
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_talks),
    ]
