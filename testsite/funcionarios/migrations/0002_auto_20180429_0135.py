# Generated by Django 2.0.3 on 2018-04-29 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario'),
        ),
    ]