from django.urls import path
from . import views


urlpatterns = [
    path('task_lists/', views.tasks_list, name='lists_of_task'),
    path('task_lists/<int:id>/', views.unique_list, name='unique'),
    path('task_lists/<int:id>/tasks/', views.task_in_list, name='unique_list_n_tasks'),
    path('tasks/<int:id>/', views.tasks, name='tasks_with_id'),
]