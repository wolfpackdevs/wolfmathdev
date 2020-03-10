from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_list, name='blog'),
    path('<int:pk>', views.post, name='post')
]
