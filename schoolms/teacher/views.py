from django.shortcuts import render,redirect
from .models import Student
from student.models import StudentLeave

from schooladmin.models import Teacher,Class,Timetable


# Create your views here.


def t_home(request):
        
    teacher = Teacher.objects.get(id =request.session['teacher_id'])
   
    return render(request,'teacher/t_home.html',{'teacher':teacher})

def profile(request):

    teacher = Teacher.objects.get(id =request.session['teacher_id'])

    return render(request,'teacher/profile.html',{'teacher':teacher})

def view_student(request):

    students = Student.objects.filter(teacher = request.session['teacher_id'])
    

    return render(request,'teacher/view_student.html',{'student_list':students})

def add_student(request):

    class_name = Class.objects.all()

    msg = ""
    if request.method == 'POST':
        s_name = request.POST['s_name']
        s_email = request.POST['s_email']
        s_dob = request.POST['s_dob']
        s_phone_number = request.POST['s_ph_no']
        s_place = request.POST['s_place']
        parent_name = request.POST['p_name']
        s_photo = request.FILES['s_photo']  
        s_password = request.POST['s_password'] 
        class_name = request.POST['class_name'] 


       #exist() not in get - only in filter -  result will be boolean
        email_exist = Student.objects.filter(student_email = s_email).exists()  

        if not email_exist:
            student = Student(
                student_name = s_name, 
                student_email = s_email, 
                student_dob = s_dob,
                student_phone_number = s_phone_number, 
                student_place = s_place, 
                s_parent_name = parent_name,
                student_profile_picture = s_photo, 
                student_password = s_password, 
                teacher_id = request.session['teacher_id'],
                student_class_id = class_name )
            student.save()
            msg = "Student added successfully"
        else:
            msg = "Student already added"

    return render(request,'teacher/add_student.html',{'status':msg,'classes':class_name})

def change_pswd(request):
   
    return render(request,'teacher/change_password.html',)


def student_leave(request):

    studentleave =StudentLeave.objects.filter(status='pending')

    if request.method == 'POST':
        s_id = request.POST['student_id']
        leave_app = StudentLeave.objects.get(id = s_id)

        if 'approve' in request.POST :
            leave_app.status = 'approved'
            leave_app.save()

        if 'reject' in request.POST  :
            leave_app.status = 'rejected'
            leave_app.save()



   
    return render(request,'teacher/students_leave.html',{'studentleave':studentleave})


def leave_apply(request):
   
    return render(request,'teacher/leave_apply.html')
def timetable(request):
    
    teacher_id = request.session['teacher_id']
    teacher_timetable = Timetable.objects.filter(teacher_id=teacher_id)

    return render(request,'teacher/timetable.html',{'teacher_timetable':teacher_timetable})



def logout(request):
    del request.session['teacher_id']
    request.session.flush()
    return redirect('common:t_login')

