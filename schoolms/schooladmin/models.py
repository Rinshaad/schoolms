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

    class Meta:
        db_table = 'teacher'







   
