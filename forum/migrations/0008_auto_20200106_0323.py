# Generated by Django 3.0.2 on 2020-01-06 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20200106_0113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_added']},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-date_added']},
        ),
    ]
