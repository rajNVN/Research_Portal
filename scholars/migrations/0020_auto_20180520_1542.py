# Generated by Django 2.0.3 on 2018-05-20 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholars', '0019_auto_20180520_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='AddedOn',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='FinishedOn',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='StartedOn',
            field=models.DateTimeField(null=True),
        ),
    ]