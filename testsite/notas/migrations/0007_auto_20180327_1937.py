# Generated by Django 2.0.3 on 2018-03-27 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0006_auto_20180325_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquery',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
