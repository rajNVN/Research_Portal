# Generated by Django 2.0.3 on 2018-05-09 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholars', '0012_auto_20180508_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='RESULT',
            fields=[
                ('Option', models.PositiveSmallIntegerField()),
                ('Scholar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='scholars.MASTERS')),
            ],
        ),
    ]