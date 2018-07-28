# Generated by Django 2.0.3 on 2018-05-08 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0008_auto_20180507_2320'),
        ('scholars', '0006_auto_20180508_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='COUNSEL',
            fields=[
                ('Option', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('Group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='guides.GROUP')),
                ('Guide', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='guides.GUIDE')),
                ('Scholar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scholars.MASTERS')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='option',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='option',
            name='Group',
        ),
        migrations.RemoveField(
            model_name='option',
            name='Guide',
        ),
        migrations.RemoveField(
            model_name='option',
            name='Scholar',
        ),
        migrations.DeleteModel(
            name='OPTION',
        ),
        migrations.AlterUniqueTogether(
            name='counsel',
            unique_together={('Scholar', 'Option')},
        ),
    ]