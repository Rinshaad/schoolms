from django.shortcuts import render
from teacher.models import Student

# Create your views here.

def s_home(request):

    student = Student.objects.filter(id= request.session['student_id']).values('student_name','student_profile_picture')
    student_name = student[0]['student_name']
    student_image = student[0]['student_profile_picture']



    return render(request,'student/s_home.html',{'name':student_name,'image':student_image})

def profile(request):
    return render(request,'student/profile.html')

def change_pswd(request):
    

    return render(request,'student/change_password.html')

