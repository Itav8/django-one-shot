from django.shortcuts import redirect, render
from todos.forms import TodoListForm

from todos.models import TodoItem, TodoList


# Create your views here.
def todo_list(request):
    todos = TodoList.objects.all()
    context = {
        "todo_list": todos,
    }
    return render(request, "todos/todo_list.html", context)


def todo_list_detail(request, id):
    item = TodoList.objects.get(id=id)
    context = {
        "task_list": item,
    }
    return render(request, "todos/todo_list_detail.html", context)


def create_todo_list(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            name = form.save()
            return redirect("todo_list_detail", id=name.id)
    else:
        form = TodoListForm()

    context = {
        "form": form,
    }
    return render(request, "todos/create.html", context)


def update_todo_list(request, id):
    todo = TodoList.objects.get(id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect("todo_list_detail", id=todo.id)
    else:
        form = TodoListForm(instance=todo)

    context = {
        "form": form
    }

    return render(request, "todos/edit.html", context)
