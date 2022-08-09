from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib import messages
from .form import TodoCreateForm, TodoUpdateForm


def Home(request):
    all = Todo.objects.all()
    return render(request, 'Home.html', context={'todos': all})


def Detail(request, id_todo):
    todo = Todo.objects.get(id=id_todo)
    return render(request, 'Detail.html', {'todo': todo})


def Delete(request, id_todo):
    Todo.objects.get(id=id_todo).delete()
    messages.success(request, 'Todo Deleted Successfully', 'success')
    return redirect('Home')


def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Todo Create Successfully', 'success')
            return redirect('Home')

    form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})


def update(request, id_todo):
    todo = Todo.objects.get(id=id_todo)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo Update Successfully', 'success')
            return redirect ('detail' , id_todo)

    else:
        form = TodoUpdateForm(instance=todo)
        return render(request, 'update.html', {'form': form})
