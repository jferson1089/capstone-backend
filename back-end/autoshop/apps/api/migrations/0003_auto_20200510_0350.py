# Generated by Django 3.0.6 on 2020-05-10 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200510_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='date_requested',
        ),
    ]
