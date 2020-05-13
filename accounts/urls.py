from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='schoolsignup'),
    path('login/', views.loginview , name='loginurl'),
    path('logout/', views.logout , name='logout')
]
