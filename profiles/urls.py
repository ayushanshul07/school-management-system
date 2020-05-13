from django.urls import path
from . import views

urlpatterns = [
    path('school/<int:school_id>/', views.schoolhome, name='homeschool'),
    path('teacher/<int:teacher_id>/', views.teacherhome, name='hometeacher'),
    path('student/<int:student_id>/', views.studenthome, name='homestudent')
]
