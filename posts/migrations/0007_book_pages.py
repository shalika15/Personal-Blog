# Generated by Django 2.0.5 on 2018-06-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20180623_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(default='250'),
        ),
    ]
