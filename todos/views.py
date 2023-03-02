from django.shortcuts import redirect, render
from todos.forms import TodoItemForm, TodoListForm

from todos.models import TodoItem, TodoList


# Create your views here.
def todo_list(request):
    todos = TodoList.objects.all()
    context = {
        "todo_list": todos,
    }
    return render(request, "todos/todo_list.html", context)


def detail_todo_list(request, id):
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

    context = {"form": form}

    return render(request, "todos/edit.html", context)


def delete_todo_list(request, id):
    todo = TodoList.objects.get(id=id)
    if request.method == "POST":
        todo.delete()
        return redirect("todo_list_list")

    return render(request, "todos/delete.html")


def create_todo_item(request):
    todos_list = TodoList.objects.all()

    if request.method == "POST":
        form = TodoItemForm(request.POST)

        if form.is_valid():
            item = form.save()
            print("ITEM", item, item.list, item.due_date)
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm()

    context = {"form": form, "todos_list": todos_list}

    return render(request, "todos/todo_item_create.html", context)
