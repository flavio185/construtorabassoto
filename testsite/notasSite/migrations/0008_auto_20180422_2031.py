# Generated by Django 2.0.3 on 2018-04-22 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0007_auto_20180419_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userquery',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserQuery',
        ),
    ]