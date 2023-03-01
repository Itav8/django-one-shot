from django.urls import path
from .views import create_todo_list, todo_list_detail, todo_list


urlpatterns = [
    path("", todo_list, name="todo_list_list"),
    path("<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("create/", create_todo_list, name="todo_list_create"),
]
