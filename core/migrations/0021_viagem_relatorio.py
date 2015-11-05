# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20151027_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='viagem',
            name='relatorio',
            field=models.TextField(null=True),
        ),
    ]
