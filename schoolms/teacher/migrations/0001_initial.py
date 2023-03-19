# Generated by Django 4.1.7 on 2023-03-14 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schooladmin', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('student_email', models.CharField(max_length=30)),
                ('student_dob', models.CharField(max_length=20)),
                ('student_phone_number', models.BigIntegerField()),
                ('student_place', models.CharField(max_length=30)),
                ('s_parent_name', models.CharField(max_length=30)),
                ('student_profile_picture', models.ImageField(upload_to='student/')),
                ('student_password', models.CharField(max_length=20)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schooladmin.teacher')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]