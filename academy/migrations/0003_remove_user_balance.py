# Generated by Django 3.0.14 on 2022-09-09 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_auto_20220909_0745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='balance',
        ),
    ]
