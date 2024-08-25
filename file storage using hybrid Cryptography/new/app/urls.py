from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
     path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
    path('download/<str:filename>/', views.download, name='download'),
]
