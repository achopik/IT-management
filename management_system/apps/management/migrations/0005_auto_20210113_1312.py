# Generated by Django 3.1.5 on 2021-01-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20210112_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='utilization_target',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
