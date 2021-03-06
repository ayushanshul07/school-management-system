import csv, os
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import REDIRECT_FIELD_NAME
from accounts.models import SchoolAdmin, Teacher, Student, Types
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied


def same_user_check(function):
    def wrap(request, *args, **kwargs):
        if kwargs['id'] == request.user.id:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def generate_username(first_name, last_name):
	val = "{0}.{1}".format(first_name,last_name).lower()
	x=0
	while True:
		if x == 0 and User.objects.filter(username=val).count() == 0:
			return val
		else:
			new_val = "{0}{1}".format(val,x)
			if User.objects.filter(username=new_val).count() == 0:
				return new_val
		x += 1

@login_required(login_url='accounts/login/')
@same_user_check
def schoolhome(request, id):
	if request.method == 'POST':
		for html_name, uploaded_file in request.FILES.items():
			myfile = request.FILES[html_name]
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.url(filename)
			uploaded_file_url = settings.BASE_DIR + uploaded_file_url

			# remove first 4 chars i.e class
			standard = html_name[5:]
			school_object = SchoolAdmin.objects.get(id=id)
			if standard == '':
				Teacher.objects.all().delete()
				with open(uploaded_file_url) as f:
					reader = csv.reader(f)
					for row in reader:
						Teacher.objects.create_user(
							first_name=row[0],
							last_name=row[2],
							email=row[3],
							username=generate_username(row[0],row[2]),
							password=generate_username(row[0],row[2]),
							school_id=school_object,
							role=Types.TEACHER)
			else:
				standard = int(standard)
				Student.objects.filter(standard=standard).delete()
				with open(uploaded_file_url) as f:
					reader = csv.reader(f)
					for row in reader:
						Student.objects.create_user(
							first_name=row[0],
							last_name=row[2],
							email=row[3],
							username=generate_username(row[0],row[2]),
							password=generate_username(row[0],row[2]),
							school_id=school_object,
							standard=standard,
							role=Types.STUDENT)
	school_object = SchoolAdmin.objects.get(id=id)
	teachers_list = Teacher.objects.filter(school_id_id=id)
	students_list = Student.objects.filter(school_id_id=id)
	class_list = [5,6,7,8,9,10]
	return render(request, 'profiles/schoolhome.html',
		{	'school_admin': school_object, 
			'teachers_list': teachers_list,
			'students_list': students_list,
			'class_list': class_list
		})

@login_required(login_url='accounts/login/')
@same_user_check
def teacherhome(request, id):
	return render(request,'profiles/teacherhome.html')

@login_required(login_url='accounts/login/')
@same_user_check
def studenthome(request, id):
	return render(request,'profiles/studenthome.html')
