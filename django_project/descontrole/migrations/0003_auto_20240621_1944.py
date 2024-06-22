# Generated by Django 3.2.25 on 2024-06-21 22:44

import descontrole.models.enum
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('descontrole', '0002_alter_estimativa_mes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimativa',
            name='natureza',
            field=models.CharField(choices=[('saida', 'Saida'), ('entrada', 'Entrada'), (descontrole.models.enum.NaturezaEnum.Meta, 'Meta')], max_length=7),
        ),
        migrations.AlterField(
            model_name='evento',
            name='natureza',
            field=models.CharField(choices=[('saida', 'Saida'), ('entrada', 'Entrada'), (descontrole.models.enum.NaturezaEnum.Meta, 'Meta')], max_length=7),
        ),
        migrations.AlterField(
            model_name='evento',
            name='tipo',
            field=models.CharField(choices=[('pix', 'Pix'), ('debito', 'Debito'), ('credito', 'Credito'), ('dinheiro', 'Dinheiro'), ('boleto', 'Boleto'), ('outros', 'Outros'), (descontrole.models.enum.TipoEnum.Meta, 'Meta')], max_length=8),
        ),
    ]