from django.urls import path, include

from todo.views import create_task, delete_task, get_tasks, task_detail, update_task

urlpatterns = [
    path('list-task/', get_tasks),
    path('detail-task/<int:id>/', task_detail),
    path('add-task/', create_task),
    path('update-task/<int:id>/', update_task),
    path('delete-task/<int:id>/', delete_task)
]