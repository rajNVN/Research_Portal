# Generated by Django 2.0.3 on 2018-05-10 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0008_auto_20180507_2320'),
        ('scholars', '0014_auto_20180510_1147'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='COUNT',
            new_name='REGISTER',
        ),
    ]
