# Generated by Django 2.0.3 on 2018-04-21 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0030_auto_20180420_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(max_length=30),
        ),
    ]
