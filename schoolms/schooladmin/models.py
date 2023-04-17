from django.db import models

# Create your models here.


class AdminLogin(models.Model):
    admin_id = models.CharField(max_length = 25)  
    admin_pswd = models.CharField(max_length = 30)


    class Meta:
        db_table = 'adminlogin'

class Teacher(models.Model):
    teacher_name = models.CharField(max_length = 25)   # varchar(25)
    teacher_email = models.CharField(max_length = 30)
    teacher_address = models.CharField(max_length = 100)
    qualification = models.CharField(max_length = 30)
    exp = models.IntegerField()
    teacher_dob = models.CharField(max_length = 100)
    teacher_gender = models.CharField(max_length = 10)    
    teacher_profile_picture = models.ImageField(upload_to = 'teacher/')
    teacher_password = models.CharField(max_length = 20)
    subject = models.CharField(max_length=50,default='')
    tutor = models.CharField(max_length=50,default='')


    class Meta:
        db_table = 'teacher'

class Notice(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    date = models.CharField(max_length=50,default='')


    class Meta:
        db_table = 'notice'


class Subject(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'subject'

class Class(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'classes'


class Timetable(models.Model):
     
    TIME_SLOT_CHOICES = (
        ('10:00 AM - 11:00 AM', '10:00 AM - 11:00 AM'),
        ('11:00 AM - 12:00 PM', '11:00 AM - 12:00 PM'),
        ('12:00 PM - 01:00 PM', '12:00 PM - 01:00 PM'),
        ('01:00 PM - 02:00 PM', '01:00 PM - 02:00 PM'),
        ('02:00 PM - 03:00 PM', '02:00 PM - 03:00 PM'),
       
    )
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=50,default='')
    time_slot = models.CharField(max_length=20, choices=TIME_SLOT_CHOICES,default='')

    class Meta:
        db_table = 'timetable'








    







   
