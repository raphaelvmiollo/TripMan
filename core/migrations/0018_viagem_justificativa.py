# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20151006_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='viagem',
            name='justificativa',
            field=models.CharField(default='', max_length=255),
            preserve_default='',
        ),
    ]
