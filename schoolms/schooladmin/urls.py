from django.urls import path

from .import views

app_name = 'schooladmin'

urlpatterns = [
  path('',views.a_home,name='home'),
  path('add_teacher',views.add_teacher,name='add_teacher'),
  path('view_teacher',views.view_teacher,name='view_teacher'),
  path('view_student',views.view_student,name='view_student'),
  path('change_password',views.change_pswd,name='change_pswd')
]