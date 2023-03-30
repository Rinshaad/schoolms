# Generated by Django 4.1.7 on 2023-03-28 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('student', '0002_alter_studentleave_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentleave',
            name='studentid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='teacher.student'),
        ),
    ]