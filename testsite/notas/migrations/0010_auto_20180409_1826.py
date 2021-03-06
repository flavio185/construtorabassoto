# Generated by Django 2.0.3 on 2018-04-09 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0009_auto_20180409_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposito',
            name='comentarios',
            field=models.CharField(blank=True, default=0, help_text='Informações relacionadas com o depósito(opcional).', max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deposito',
            name='data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='deposito',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
