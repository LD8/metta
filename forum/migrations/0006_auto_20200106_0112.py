# Generated by Django 3.0.2 on 2020-01-06 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_added']},
        ),
    ]
