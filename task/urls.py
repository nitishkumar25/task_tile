from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.task_form,name='task_insert'), #get and post req for insert operations
    path('<int:id>/', views.task_form,name='task_update'),#get and post req for update operations
    path('delete/<int:id>/',views.task_delete,name='task_delete'),
    path('list/',views.task_list,name='task_list')#get req to display and retrieve all records
]