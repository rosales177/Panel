from os import name
from django.urls import path
from .views import Create, Crud, Delete, Update, index

app_name = 'app'

urlpatterns = [
    path('',index,name='index'),
    path('delete_<int:id>/',Delete,name='delete'),
    path('crud',Crud,name='crud'),
    path('create',Create,name='create'),
    path('update_<int:id>/',Update,name='update')
]
