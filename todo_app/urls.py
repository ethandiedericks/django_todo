from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('updateTask/<task_id>', views.updateTask, name='updateTask'),
    path('deleteTask/<task_id>', views.deleteTask, name='deleteTask'),
]