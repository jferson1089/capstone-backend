# Generated by Django 3.0.6 on 2020-05-12 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200512_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_requested',
            field=models.DateTimeField(null=True),
        ),
    ]
