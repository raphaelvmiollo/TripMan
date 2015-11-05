# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150922_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='matricula_siape',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
