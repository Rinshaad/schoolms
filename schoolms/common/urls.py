from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('',views.home,name='home'),
    path('admin_login',views.a_login,name='a_login'),
    path('a_signup',views.a_signup,name='a_signup'),

    path('student_login',views.s_login,name='s_login'),
    path('teacher_login',views.t_login,name='t_login')    
]