from django.db import models
from teacher.models import Student

# Create your models here.

from django.db import models

class StudentLeave(models.Model):

    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    reason = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE,default=None)
    status = models.CharField(max_length = 20, default = 'pending')
    

    class Meta:
        db_table = 'studentleave'

