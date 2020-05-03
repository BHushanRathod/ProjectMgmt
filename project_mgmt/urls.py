from django.urls import path
from . import views

urlpatterns = [
    path('<int:proj_id>/task/<int:task_id>/subtask/<int:subtask_id>', views.SubTaskDetails.as_view()),
    path('<int:proj_id>/task/<int:task_id>/subtask/', views.SubTaskDetails.as_view()),
    path('<int:proj_id>/task/<int:task_id>', views.TaskDetailsList.as_view()),
    path('<int:proj_id>/task/', views.TaskDetailsList.as_view()),
    path('<int:proj_id>/', views.ProjectDetailsList.as_view()),
    path('', views.ProjectDetailsList.as_view())
    # path('pid', views.ProjectDetails.as_view(), name='project_detail'),
    # path(r'task', views.TaskMgnt.as_view()),
    # path(r'^pid/', views.ProjectDetails.as_view()),
]