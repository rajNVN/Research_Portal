# Generated by Django 2.0.3 on 2018-05-08 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholars', '0009_auto_20180508_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='counsel',
            name='id',
            field=models.AutoField(auto_created=True, default=12, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='counsel',
            name='Scholar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scholars.MASTERS'),
        ),
    ]
