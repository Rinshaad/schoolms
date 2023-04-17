from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
  path('home',views.s_home,name='home'),
  path('profile',views.profile,name='profile'),
  path('change_password',views.change_pswd,name='change_pswd'),
  path('logout',views.logout,name='logout'),
  path('leaveapply',views.leave_apply,name='leave_apply'),
  path('notices',views.notices,name='notices'),
  path('leaveapp',views.leaveapplications,name='leaveapp'),
  path('timetable',views.timetable,name='timetable'),
  path('get_data',views.get_data, name='get_data')






  


]