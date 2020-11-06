from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
   
    path('', views.login,name='login'),
    path('home', views.home,name='home'),
    path('list', views.list,name='list'),
    path('edit/<str:pk>/',views.edit,name='edit'),
    path('delete/<str:pk>/',views.delete,name='delete'),
    path('images/<str:pk>/',views.image,name='image'),
    path('register',views.user_register,name='register'),
    path('logout',views.logout,name='logout')
   
]
