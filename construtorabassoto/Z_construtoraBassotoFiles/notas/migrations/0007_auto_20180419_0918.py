# Generated by Django 2.0.3 on 2018-04-19 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0006_auto_20180419_0711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nota',
            options={'ordering': ['data'], 'permissions': (('can_change', 'Pode alterar notas'),)},
        ),
    ]
