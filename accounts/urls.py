from django.urls import path 
from . import views


urlpatterns = [
    path('register/',views.UserRegister, name='register'),
    path('',views.UserLogin , name='login'),
    path('logout/',views.UserLogout , name='logout')
]
