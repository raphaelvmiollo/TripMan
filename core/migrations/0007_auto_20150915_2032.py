# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150915_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='localidade',
            name='latitude',
            field=models.CharField(default=b'', max_length=254),
        ),
        migrations.AddField(
            model_name='localidade',
            name='longitude',
            field=models.CharField(default=b'', max_length=254),
        ),
        migrations.AddField(
            model_name='viagem',
            name='passageiros',
            field=models.ManyToManyField(to='core.Passageiro', null=True),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='aprovador',
            field=models.ForeignKey(related_name='aprovador', default=b'', to='core.Usuario'),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='localidade_chegada',
            field=models.ForeignKey(related_name='chegada', default=b'', to='core.Localidade'),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='localidade_saida',
            field=models.ForeignKey(related_name='saida', default=b'', to='core.Localidade'),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='motorista',
            field=models.ForeignKey(related_name='motorista', default=b'', to='core.Usuario'),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='solicitante',
            field=models.ForeignKey(related_name='solicitante', default=b'', to='core.Usuario'),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='veiculo',
            field=models.ForeignKey(default=b'', to='core.Veiculo'),
        ),
    ]
