# Generated by Django 3.1.2 on 2020-10-09 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20201009_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editor',
            name='phone_number',
        ),
    ]
