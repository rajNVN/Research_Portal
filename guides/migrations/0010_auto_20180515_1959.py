# Generated by Django 2.0.3 on 2018-05-15 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0009_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='type',
            new_name='is_Guide',
        ),
    ]
