# Generated by Django 2.0.3 on 2018-05-07 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0007_delete_sample'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide',
            name='MailId',
        ),
        migrations.RemoveField(
            model_name='guide',
            name='Password',
        ),
    ]