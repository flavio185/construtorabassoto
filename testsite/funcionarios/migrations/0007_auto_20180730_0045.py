# Generated by Django 2.0.3 on 2018-07-30 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0006_auto_20180628_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagamento',
            name='extra',
        ),
        migrations.RemoveField(
            model_name='pagamento',
            name='funcionario',
        ),
        migrations.AddField(
            model_name='pagamento',
            name='tipo',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
