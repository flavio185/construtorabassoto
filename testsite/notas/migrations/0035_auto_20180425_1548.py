# Generated by Django 2.0.3 on 2018-04-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0034_auto_20180425_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresaservico',
            name='descricao',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
