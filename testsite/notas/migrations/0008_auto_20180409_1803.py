# Generated by Django 2.0.3 on 2018-04-09 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0007_auto_20180327_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
                ('comentarios', models.CharField(help_text='Informações relacionadas com o depósito(opcional).', max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='nota',
            name='deposito',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notas.Deposito'),
        ),
    ]
