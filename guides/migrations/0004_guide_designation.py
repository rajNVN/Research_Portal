# Generated by Django 2.0.3 on 2018-04-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0003_auto_20180428_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='Designation',
            field=models.CharField(default='proffessor', max_length=30),
        ),
    ]
