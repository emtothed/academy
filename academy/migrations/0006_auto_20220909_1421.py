# Generated by Django 3.0.14 on 2022-09-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0005_auto_20220909_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='passed',
            field=models.ManyToManyField(blank=b'I01\n', to='academy.Course'),
        ),
    ]
