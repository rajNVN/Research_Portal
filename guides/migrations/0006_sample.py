# Generated by Django 2.0.3 on 2018-05-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0005_auto_20180502_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ik', models.IntegerField()),
            ],
        ),
    ]
