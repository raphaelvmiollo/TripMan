# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20151006_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='aprovador',
            field=models.ForeignKey(related_name='aprovador', default=b'', to='core.Usuario', null=True),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='motorista',
            field=models.ForeignKey(related_name='motorista', default=b'', to='core.Usuario', null=True),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='solicitante',
            field=models.ForeignKey(related_name='solicitante', default=b'', to='core.Usuario', null=True),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='status',
            field=models.CharField(max_length=1),
        ),
    ]
