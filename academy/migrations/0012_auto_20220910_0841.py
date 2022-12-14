# Generated by Django 3.0.14 on 2022-09-10 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0011_auto_20220910_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(related_name='students', to='academy.Course'),
        ),
        migrations.AlterField(
            model_name='user',
            name='passed',
            field=models.ManyToManyField(related_name='passedstudents', to='academy.Course'),
        ),
    ]
