# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20151006_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='TipoVeiculo',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='numAssentos',
        ),
    ]
