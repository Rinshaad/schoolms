# Generated by Django 4.1.7 on 2023-03-28 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_studentleave_studentid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentleave',
            name='studentid',
        ),
    ]
