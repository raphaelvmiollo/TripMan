# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20151006_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='TipoVeiculo',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='numAssentos',
            field=models.IntegerField(default=0),
        ),
    ]
