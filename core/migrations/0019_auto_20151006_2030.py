# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_viagem_justificativa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='justificativa',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
