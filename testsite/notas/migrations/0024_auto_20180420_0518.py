# Generated by Django 2.0.3 on 2018-04-20 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0023_auto_20180420_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(max_length=30),
        ),
    ]
