# Generated by Django 2.0.3 on 2018-04-29 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('data_nascimento', models.DateField(blank=True)),
                ('cpf', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('rg', models.CharField(blank=True, max_length=12)),
                ('endereco', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=60)),
                ('estado', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=15)),
                ('telefone2', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ativo', models.BooleanField(default=True, verbose_name='ativo')),
                ('imagem', models.FileField(blank=True, upload_to='notas_compras')),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('extra', models.BooleanField()),
                ('comentario', models.CharField(max_length=60)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.Funcionario')),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='ocupacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='funcionarios.Ocupacao'),
        ),
    ]