# Generated by Django 2.0.3 on 2018-04-20 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0017_auto_20180419_0613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nota',
            options={'ordering': ['data'], 'permissions': (('can_change', 'Pode alterar notas'),)},
        ),
    ]
