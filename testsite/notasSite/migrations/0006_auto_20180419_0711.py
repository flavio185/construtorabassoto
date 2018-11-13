# Generated by Django 2.0.3 on 2018-04-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0005_auto_20180418_1849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nota',
            options={'permissions': (('can_change', 'Pode alterar notas'),)},
        ),
        migrations.AddField(
            model_name='nota',
            name='projeto',
            field=models.CharField(choices=[('Marina', 'MARINA'), ('Casa_de_Eventos', 'CASA DE EVENTOS')], default='Marina', max_length=20),
        ),
    ]