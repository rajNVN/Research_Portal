# Generated by Django 2.0.3 on 2018-05-08 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholars', '0010_auto_20180508_1454'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='counsel',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='counsel',
            name='Group',
        ),
        migrations.RemoveField(
            model_name='counsel',
            name='Guide',
        ),
        migrations.RemoveField(
            model_name='counsel',
            name='Scholar',
        ),
        migrations.RemoveField(
            model_name='scholar',
            name='Counsel',
        ),
        migrations.DeleteModel(
            name='COUNSEL',
        ),
    ]
