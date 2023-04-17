from django.shortcuts import render
from .models import Teacher,Notice,Subject,Class,Timetable
from teacher.models import Student
from .models import AdminLogin




# Create your views here.



def a_home(request):

    notices = Notice.objects.all()
    return render(request,'schooladmin/a_home.html',{'notices':notices})

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
    students = Student.objects.all()
    return render(request,'schooladmin/view_student.html',{'students':students})

def view_teacher(request):

    teachers = Teacher.objects.all()

    return render(request,'schooladmin/view_teachers.html',{'teacher_list':teachers})

def change_pswd(request):
    msg =''
    if request.method == 'POST':
        oldpass = request.POST['oldpass']
        newpass = request.POST['newpass']
        confirmpass = request.POST['confirmpass']

        admin = AdminLogin.objects.get(id=1)
        
        if admin.admin_pswd == oldpass :
            if newpass == confirmpass :
                admin = AdminLogin.objects.filter(id =1).update(admin_pswd =newpass)
                

            else:
                msg = 'password not matching'

        else:
            msg='your password is incorrect'


    return render(request,'schooladmin/change_password.html',{'msg':msg})

def subjects(request):

    msg = ''

    if request.method == 'POST':
        subject_name = request.POST['subject_name']

        subject = Subject(name = subject_name)
        subject.save()

        msg= 'added successfully'

    subjects = Subject.objects.all()

    return render(request,'schooladmin/subjects.html',{'msg':msg,'subjects':subjects})

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

def notice(request):
    msg = ''

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        date = request.POST['date']


        notice = Notice(title = title ,content = content,date = date)
        notice.save()
        msg = 'posted successfully'

    return render(request,'schooladmin/notice.html',{'msg':msg})



def add_timetable(request):

    classes = Class.objects.all()
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()


    msg =''
    if request.method == 'POST':
        day_of_week = request.POST['day_of_week']
        time_slot = request.POST['time_slot']
        subject = request.POST['subject']
        class_name = request.POST['class_name']
        teacher = request.POST['teacher']

        existing_timetable = Timetable.objects.filter(day_of_week=day_of_week, time_slot=time_slot, class_name_id=class_name).exists()

        if not existing_timetable:

            timetable = Timetable(day_of_week = day_of_week,time_slot = time_slot , subject_id = subject ,class_name_id =class_name ,teacher_id = teacher)
            timetable.save()

            msg ='added successfully'

        else:
            msg = 'In this time and day already added'

    context = {
        'subjects':subjects,
        'teachers':teachers,
        'classes':classes,
        'msg':msg,
        'time_slot_choices': Timetable.TIME_SLOT_CHOICES


    }


    return render(request,'schooladmin/add_timetable.html',context)


def add_class(request):

    msg = ''

    if request.method == 'POST':
        class_name = request.POST['class_name']

        clas = Class(name = class_name)
        clas.save()
        msg= 'added successfully'


    classes = Class.objects.all()

    return render(request,'schooladmin/add_classes.html',{'msg':msg,'classes':classes})

def timetable(request):

    timetable = Timetable.objects.filter(day_of_week__in=['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
    weekdays = {'monday': [], 'tuesday': [], 'wednesday': [], 'thursday': [], 'friday': []}

    for entry in timetable:
        weekdays[entry.day_of_week].append(entry)

    return render(request,'schooladmin/timetable.html',{'timetable':weekdays})
