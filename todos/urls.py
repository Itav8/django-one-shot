from django.urls import path
from .views import (
    create_todo_item,
    create_todo_list,
    delete_todo_list,
    detail_todo_list,
    todo_list,
    update_todo_item,
    update_todo_list,
)


urlpatterns = [
    path("", todo_list, name="todo_list_list"),
    path("<int:id>/", detail_todo_list, name="todo_list_detail"),
    path("create/", create_todo_list, name="todo_list_create"),
    path("<int:id>/edit/", update_todo_list, name="todo_list_update"),
    path("<int:id>/delete/", delete_todo_list, name="todo_list_delete"),
    path("items/create", create_todo_item, name="todo_item_create"),
    path("items/<int:id>/edit/", update_todo_item, name="todo_item_update"),
]
