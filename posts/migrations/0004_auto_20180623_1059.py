# Generated by Django 2.0.5 on 2018-06-23 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180621_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='price_Book',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
