# Generated by Django 2.0.3 on 2018-06-28 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0005_auto_20180628_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValeTransporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='vale_transporte',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='funcionarios.ValeTransporte'),
        ),
    ]
