# Generated by Django 2.0.3 on 2018-03-27 22:09

from django.db import migrations, models
import notas.models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0006_auto_20180325_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='imagem',
            field=models.FileField(blank=True, upload_to=notas.models.f),
        ),
    ]