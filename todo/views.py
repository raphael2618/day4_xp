from django.shortcuts import render, redirect
from .models import Category, Todo
from .form import TodoForm


# # Create your views here.
def display_view(request):
    return render(request, 'todo.html', {'categories': Category.objects.all()})


def form_views(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            task = Todo.objects.create(**form.cleaned_data)
            return redirect('add_task.html', task)

    if request.method == 'GET':
        form = TodoForm()
    return render(request, 'add_task.html', {'form': form})
