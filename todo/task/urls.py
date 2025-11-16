
from django.urls import path
from .views import task_list,task_detail,task_delete,task_mark_compleated,register,task_create,user_login,logout_view
urlpatterns = [
    path('',task_list,name='task_list'), 
    path('create/',task_create,name='taskCreate'),
    path('task/<int:task_id>',task_detail,name='task_detail'),
    path('task/<int:task_id>/delete/',task_delete,name='task_delete'),
    path('task/<int:task_id>/compleate/',task_mark_compleated,name='mark_compleate'),
    path('register/',register,name='register'),
    path('login/',user_login,name='login'),
    path('logout/',logout_view,name = 'logout')
]
