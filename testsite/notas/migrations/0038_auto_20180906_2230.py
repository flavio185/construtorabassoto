# Generated by Django 2.0.3 on 2018-09-07 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0037_auto_20180906_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='servico_terceirizado',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notas.ServicoTerceirizado'),
        ),
    ]