# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20151006_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='justificativa',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
