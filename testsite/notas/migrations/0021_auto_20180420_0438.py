# Generated by Django 2.0.3 on 2018-04-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0020_auto_20180420_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='nome_projeto',
            field=models.CharField(choices=[('Marina', 'MARINA'), ('Casa_de_Eventos', 'CASA DE EVENTOS')], default='Marina', max_length=30),
        ),
    ]
