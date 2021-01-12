# Generated by Django 3.1.5 on 2021-01-12 08:58

from django.db import migrations, models
import django.db.models.deletion
import management.models.choices


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='working_department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('SECURED', 'Secured')], default=management.models.choices.PositionStatus['ACTIVE'], max_length=20),
        ),
    ]