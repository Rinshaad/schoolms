# Generated by Django 4.1.7 on 2023-04-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooladmin', '0008_timetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='day_of_week',
            field=models.CharField(default='', max_length=50),
        ),
    ]
