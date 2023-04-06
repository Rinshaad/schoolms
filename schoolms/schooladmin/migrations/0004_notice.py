# Generated by Django 4.1.7 on 2023-03-31 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooladmin', '0003_teacher_tutor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'notice',
            },
        ),
    ]
