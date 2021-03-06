# Generated by Django 2.0.3 on 2018-05-25 14:37

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
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('cpf', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('rg', models.CharField(max_length=12)),
                ('endereco', models.CharField(blank=True, max_length=150, null=True)),
                ('cidade', models.CharField(blank=True, max_length=60, null=True)),
                ('estado', models.CharField(blank=True, max_length=20, null=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('telefone2', models.CharField(blank=True, max_length=15, null=True)),
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
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('extra', models.BooleanField()),
                ('comentario', models.CharField(blank=True, max_length=60, null=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios_teste.Funcionario')),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='ocupacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='funcionarios_teste.Ocupacao'),
        ),
    ]
