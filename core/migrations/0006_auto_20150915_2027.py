# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150915_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='viagem',
            name='aprovador',
            field=models.ForeignKey(related_name='aprovador', default=None, to='core.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viagem',
            name='localidade_chegada',
            field=models.ForeignKey(related_name='chegada', default='', to='core.Localidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viagem',
            name='localidade_saida',
            field=models.ForeignKey(related_name='saida', default=None, to='core.Localidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viagem',
            name='motorista',
            field=models.ForeignKey(related_name='motorista', default=None, to='core.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viagem',
            name='solicitante',
            field=models.ForeignKey(related_name='solicitante', default='', to='core.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='viagem',
            name='veiculo',
            field=models.ForeignKey(default='', to='core.Veiculo'),
            preserve_default=False,
        ),
    ]
