from django.shortcuts import render

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
