# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cargousuario_tipousuario_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Passageiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('matricula_siape', models.CharField(max_length=20)),
                ('identidade', models.CharField(max_length=20)),
                ('cargoUsuario', models.ForeignKey(to='core.CargoUsuario')),
            ],
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datahora_saida', models.DateTimeField()),
                ('datahora_chegada', models.DateTimeField()),
                ('objetivo', models.TextField()),
                ('observacoes', models.TextField()),
                ('despesa_responsavel', models.CharField(max_length=50)),
                ('ramal_contato', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='senha',
            field=models.CharField(default='admin', max_length=45),
            preserve_default=False,
        ),
    ]
