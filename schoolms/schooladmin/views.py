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
        t_subject = request.POST['t_subject'] 
        t_standard = request.POST['t_standard'] 



        teacher = Teacher(teacher_name = t_name, teacher_email = t_email, teacher_address = t_address, 
        qualification = t_qualification, teacher_dob = t_dob, teacher_gender = t_gender, exp = t_exp, 
        teacher_profile_picture = t_photo, teacher_password = t_password, subject = t_subject , tutor = t_standard) 

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

def edit_teachers(request,t_id):

    success_msg=''

    
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
        t_subject = request.POST['t_subject'] 
        t_standard = request.POST['t_standard'] 

        tid = Teacher.objects.filter(id=t_id).update(teacher_name = t_name, teacher_email = t_email, teacher_address = t_address, 
        qualification = t_qualification, teacher_dob = t_dob, teacher_gender = t_gender, exp = t_exp, 
        teacher_profile_picture = t_photo, teacher_password = t_password, subject = t_subject , tutor = t_standard)


        

        

    success_msg ='teacher updated successfully'

    return render(request,'schooladmin/edit_teachers.html',{'success_msg':success_msg})
