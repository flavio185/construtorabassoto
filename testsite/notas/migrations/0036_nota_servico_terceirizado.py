# Generated by Django 2.0.3 on 2018-09-01 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0035_auto_20180425_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='servico_terceirizado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notas.ServicoTerceirizado'),
        ),
    ]
