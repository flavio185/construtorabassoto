# Generated by Django 2.0.3 on 2018-09-09 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0052_nota_servico_terceirizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='servico_terceirizado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notas.ServicoTerceirizado'),
        ),
    ]
