from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
  path('',views.t_home,name='home'),
  path('profile',views.profile,name='profile'),
  path('add_student',views.add_student,name='add_student'),
  path('view_student',views.view_student,name='view_student'),
  path('change_password',views.change_pswd,name='change_pswd'),
  path('studentleave',views.student_leave,name='student_leave'),
  path('leaveapply',views.leave_apply,name='leave_apply'),


]