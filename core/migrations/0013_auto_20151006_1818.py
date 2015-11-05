# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150922_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='numAssentos',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='TipoVeiculo',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='TipoVeiculo',
        ),
    ]
