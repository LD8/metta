# Generated by Django 3.0.2 on 2020-01-03 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='date_created',
        ),
    ]
