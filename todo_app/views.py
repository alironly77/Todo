from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def Home(requste):
    all = Todo.objects.all()
    return render(requste, 'Home.html', context={'all':all})


def say_hello(requste):
    return render(requste , 'hello.html',{'name':'ali'} )
