# Generated by Django 4.1.7 on 2023-03-14 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooladmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=25)),
                ('teacher_email', models.CharField(max_length=30)),
                ('teacher_address', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=30)),
                ('exp', models.IntegerField()),
                ('teacher_dob', models.CharField(max_length=100)),
                ('teacher_gender', models.CharField(max_length=10)),
                ('teacher_profile_picture', models.ImageField(upload_to='teacher/')),
                ('teacher_password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]