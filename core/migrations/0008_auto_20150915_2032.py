# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150915_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localidade',
            name='longitude',
            field=models.CharField(max_length=254),
        ),
    ]
