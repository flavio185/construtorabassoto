# Generated by Django 2.0.3 on 2018-04-20 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0026_auto_20180420_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10),
        ),
    ]