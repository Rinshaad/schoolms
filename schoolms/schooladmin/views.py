from django.shortcuts import render
from .models import Teacher

# Create your views here.



def a_home(request):
    return render(request,'schooladmin/a_home.html')

def add_teacher(request):

    success_msg =''

    if request.method == 'POST':
        t_name = request.POST['t_name']
        t_email = request.POST['t_email']
        t_address = request.POST['t_address']
        t_qualification = request.POST['t_qualification']
        t_dob = request.POST['t_dob']
        t_gender = request.POST['t_gender']
        t_exp = request.POST['t_exp']
        t_photo = request.FILES['t_photo']  
        t_password = request.POST['t_password'] 

        teacher = Teacher(teacher_name = t_name, teacher_email = t_email, teacher_address = t_address, 
        qualification = t_qualification, teacher_dob = t_dob, teacher_gender = t_gender, exp = t_exp, 
        teacher_profile_picture = t_photo, teacher_password = t_password) 

        teacher.save()

        success_msg ='teacher added successfully'
   
    return render(request,'schooladmin/add_teacher.html',{'success_msg':success_msg})

def view_student(request):
    return render(request,'schooladmin/view_student.html')

def view_teacher(request):

    teachers = Teacher.objects.all()

    return render(request,'schooladmin/view_teachers.html',{'teacher_list':teachers})

def change_pswd(request):
    return render(request,'schooladmin/change_password.html')
