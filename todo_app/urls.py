from django.urls import path 
from . import views

urlpatterns = [
    path('Home/',views.Home , name='Home'),
    path('Detail/<int:id_todo>',views.Detail,name='detail'),
    path('Delete/<int:id_todo>',views.Delete,name='delete'),
    path('Create/',views.create,name='create'),
    path('Update/<int:id_todo>',views.update , name='update'),
]