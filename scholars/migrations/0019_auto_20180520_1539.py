# Generated by Django 2.0.3 on 2018-05-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholars', '0018_auto_20180520_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='FinishedOn',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='paper',
            name='StartedOn',
            field=models.DateTimeField(default=None),
        ),
    ]
