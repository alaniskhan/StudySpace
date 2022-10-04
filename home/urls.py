from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('createChapter/', views.create, name='create'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout,name='logout'),
    path('search/', views.search, name='search'), 
    path('delete/<int:id>', views.delete, name='delete'), 
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/editrecord/<int:id>', views.editrecord, name='editrecord')
]