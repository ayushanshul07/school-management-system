from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, User
from enumfields import EnumField
from enum import Enum
from django.conf import settings

class SchoolAdminManager(UserManager):
    pass

class TeacherManager(UserManager):
    pass

class StudentManager(UserManager):
    pass

class Types(Enum):
    ADMIN = 'admin'
    TEACHER = 'teacher'
    STUDENT = 'student'


class SchoolAdmin(User):
    address = models.TextField()
    school_name = models.CharField(max_length=101)
    image = models.ImageField(upload_to='images/')
    role = EnumField(Types)


class Teacher(User):
	school_id = models.ForeignKey(
		SchoolAdmin,
		on_delete=models.CASCADE)
	role = EnumField(Types)
	

class Student(User):
	school_id = models.ForeignKey(
		SchoolAdmin,
		on_delete=models.CASCADE)
	standard = models.IntegerField(blank=True, null=True)
	role = EnumField(Types)

	
	
