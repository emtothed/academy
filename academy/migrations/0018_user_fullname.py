# Generated by Django 3.0.14 on 2022-09-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0017_auto_20220914_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(default='mohammad asadi', max_length=50),
            preserve_default=False,
        ),
    ]
