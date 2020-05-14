from django.urls import path
from . import views

urlpatterns = [
    path('school/<int:id>/', views.schoolhome, name='homeschool'),
    path('teacher/<int:id>/', views.teacherhome, name='hometeacher'),
    path('student/<int:id>/', views.studenthome, name='homestudent')
]
