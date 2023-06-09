# Generated by Django 4.1.7 on 2023-03-28 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=20)),
                ('class_name', models.CharField(max_length=50)),
                ('reason', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'studentelave',
            },
        ),
    ]
