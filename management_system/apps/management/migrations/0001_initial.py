# Generated by Django 3.1.5 on 2021-01-08 16:27

from django.db import migrations, models
import django.db.models.deletion
import management.models.choices


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('utilization_current', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default=management.models.choices.Sex['MALE'], max_length=8)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('job_title', models.CharField(max_length=255)),
                ('job_level', models.CharField(max_length=100)),
                ('employment_start_date', models.DateField(auto_now_add=True)),
                ('employment_duration', models.PositiveIntegerField(verbose_name='employment duration in days')),
                ('military_eligibility', models.BooleanField(default=True)),
                ('military_served', models.BooleanField(default=True)),
                ('military_defferal_status', models.BooleanField(default=True)),
                ('military_defferal_end_date', models.DateField(blank=True, null=True)),
                ('utilization_rate', models.PositiveSmallIntegerField(verbose_name="percent of employee's utilization")),
                ('workload', models.PositiveSmallIntegerField(verbose_name="percent of employee's workload")),
                ('role', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('utilization_current', models.PositiveSmallIntegerField()),
                ('lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('office', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Technology',
                'verbose_name_plural': 'Technologies',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255, verbose_name='A certain skill description')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.technology')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=255)),
                ('partner_contact', models.URLField()),
                ('description', models.TextField()),
                ('site_link', models.URLField()),
                ('type', models.CharField(max_length=100)),
                ('account_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.employee')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.department')),
                ('project_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_project', to='management.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('assignee_name', models.CharField(max_length=255)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status_supervisor', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('OCCUPIED', 'Occupied'), ('PENDING', 'Pending')], default=management.models.choices.PositionStatus['ACTIVE'], max_length=20)),
                ('english_level', models.CharField(choices=[('NO', 'No'), ('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], default=management.models.choices.EnglishLevel['B2'], max_length=30)),
                ('assignment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.employee')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.location')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.project')),
                ('supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervised_position', to='management.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_logo', models.FileField(blank=True, null=True, upload_to='')),
                ('customer_name', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('priority', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], max_length=20)),
                ('project_start_date', models.DateField(auto_now_add=True)),
                ('project_duration', models.PositiveIntegerField(verbose_name='project duration in days')),
                ('opportunity_probability', models.PositiveSmallIntegerField(verbose_name='Opportunity probability rate in percents')),
                ('technology_name', models.CharField(max_length=255)),
                ('domain_name', models.CharField(max_length=255)),
                ('sales_name', models.CharField(max_length=255)),
                ('delivery_supervisor_name', models.CharField(max_length=255)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.location')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='management.project', verbose_name='related project')),
                ('staffing_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staffed_opportunity', to='management.location')),
            ],
            options={
                'verbose_name': 'Opportunity',
                'verbose_name_plural': 'Opportunities',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.location'),
        ),
        migrations.AddField(
            model_name='employee',
            name='main_technology',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.technology'),
        ),
        migrations.AddField(
            model_name='employee',
            name='technology_skills',
            field=models.ManyToManyField(to='management.Skill'),
        ),
        migrations.AddField(
            model_name='department',
            name='head',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_department', to='management.employee'),
        ),
        migrations.AddField(
            model_name='department',
            name='resource_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.employee'),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='management.group')),
                ('utilization_target', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.technology')),
            ],
            bases=('management.group',),
        ),
    ]