# Generated by Django 4.1.7 on 2023-04-12 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schooladmin', '0010_remove_timetable_time_of_day_timetable_time_slot'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schooladmin.class'),
        ),
    ]