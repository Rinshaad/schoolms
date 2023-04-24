from django.shortcuts import render,redirect
from teacher.models import Student
from .models import StudentLeave
from schooladmin.models import Notice ,Timetable,Teacher
from django.http import JsonResponse


# Create your views here.

def s_home(request):
    student_d=Student.objects.get(id=request.session['student_id'])

    return render(request,'student/s_home.html',{'s_details':student_d})
   


def profile(request):

    student_d=Student.objects.get(id=request.session['student_id'])

    return render(request,'student/profile.html',{'s_details':student_d})



def change_pswd(request):


    msg = ""
    if request.method == 'POST':
        s_old_pwd = request.POST['old_pwd']
        s_new_pwd = request.POST['new_pwd']
        s_confirm_pwd = request.POST['confirm_pwd']

        student = Student.objects.get(id = request.session['student_id'])
        if student.student_password == s_old_pwd:
            if s_new_pwd == s_confirm_pwd:
                Student.objects.filter(id = request.session['student_id']).update(student_password = s_new_pwd)
                # student.student_password = s_new_pwd
                # student.save()
                msg = "Password changed successfully"
            else:
                msg = "Password does not match"
        else:
            msg = "incorrect password"

    return render(request,'student/change_password.html',{'status':msg})



def logout(request):
    del request.session['student_id']
    request.session.flush()
    return redirect('common:s_login')




def leave_apply(request):

    status = ''

    if request.method == 'POST':

        name =request.POST['name']
        standard =request.POST['class']
        reason =request.POST['reason']
        start_date =request.POST['start_date']
        end_date =request.POST['end_date']
        s_id =request.session['student_id']

        leave = StudentLeave(name=name ,class_name = standard, reason = reason,start_date =start_date,end_date =end_date ,student_id =s_id )

        leave.save()
        



    return render(request,'student/leave_apply.html',{'status':'sent successfully'})

def notices(request):

    notices = Notice.objects.all().order_by('-id')


    return render(request,'student/notices.html',{'notices':notices})

def leaveapplications(request):

    s_id = request.session['student_id']

    leave_apps = StudentLeave.objects.filter(student_id = s_id)


    return render(request,'student/leave_applications.html',{'leave_apps':leave_apps})




def timetable(request):

    student_id = request.session['student_id']
    student_class = Student.objects.get(id=student_id).student_class.id
    
   
    timetable = Timetable.objects.filter(day_of_week__in=['monday', 'tuesday', 'wednesday', 'thursday', 'friday'],class_name_id =student_class)
    weekdays = {'monday': [], 'tuesday': [], 'wednesday': [], 'thursday': [], 'friday': []}

    for entry in timetable:
        weekdays[entry.day_of_week].append(entry)

  
    return render(request,'student/timetable.html',{'timetable':weekdays})

   

    

def get_data(request):
    timetable_data = list(Timetable.objects.values())
    return JsonResponse(timetable_data, safe=False)


