from django.urls import path
from teach import views

urlpatterns = [
    path('', views.teach_list, name='teach'),
]
