# Generated by Django 2.0.3 on 2018-04-21 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0031_auto_20180420_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='projeto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notas.Projeto'),
        ),
    ]