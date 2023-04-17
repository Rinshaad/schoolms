from django.urls import path

from .import views

app_name = 'schooladmin'

urlpatterns = [
  path('',views.a_home,name='home'),
  path('add_teacher',views.add_teacher,name='add_teacher'),
  path('view_teacher',views.view_teacher,name='view_teacher'),
  path('view_student',views.view_student,name='view_student'),
  path('change_password',views.change_pswd,name='change_pswd'),
  path('edit_teacher/<int:t_id>',views.edit_teachers,name='edit_teachers'),
  path('notice',views.notice,name='notice'),
  path('subjects',views.subjects,name='subjects'),
  path('add_timetable',views.add_timetable,name='add_timetable'),
  path('add_class',views.add_class,name='add_class'),
  path('timetable',views.timetable,name='timetable'),






]