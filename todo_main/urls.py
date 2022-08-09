from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',include('todo_app.urls')),
    path('',include('accounts.urls')),
]
