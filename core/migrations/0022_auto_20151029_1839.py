# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_viagem_relatorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='relatorio',
            field=models.TextField(null=True, blank=True),
        ),
    ]
