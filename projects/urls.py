from django.urls import path
from projects import views

# app_name = 'programmer'

urlpatterns = [
    path('', views.projects_list, name='projects'),
    path('<int:pk>', views.project_detail, name='project_detail')
]
