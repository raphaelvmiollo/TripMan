# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_viagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoVeiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=30)),
                ('qtdLugares', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(max_length=8)),
                ('marca', models.CharField(max_length=30)),
                ('banheiro', models.BooleanField()),
                ('potencia', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('manutencao', models.BooleanField()),
                ('TipoVeiculo', models.ForeignKey(to='core.TipoVeiculo')),
            ],
        ),
        migrations.RemoveField(
            model_name='viagem',
            name='localidadeDestino',
        ),
        migrations.DeleteModel(
            name='Localidade',
        ),
        migrations.DeleteModel(
            name='Viagem',
        ),
    ]
