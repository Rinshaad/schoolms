from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
  path('',views.s_home,name='home'),
  path('profile',views.profile,name='profile'),
  path('change_password',views.change_pswd,name='change_pswd')
]