# Generated by Django 2.0.3 on 2018-09-07 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        
        ('notas', '0042_auto_20180907_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='servico_terceirizado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicos_terceirizados.ServicoTerceirizado'),
        ),
    ]
