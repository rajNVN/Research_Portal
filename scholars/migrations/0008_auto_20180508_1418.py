# Generated by Django 2.0.3 on 2018-05-08 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholars', '0007_auto_20180508_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholar',
            name='Counsel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scholars.COUNSEL'),
        ),
        migrations.DeleteModel(
            name='A_SCHOLAR',
        ),
    ]
