from django.contrib.auth import login, authenticate, logout as django_logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SchoolAdmin, Teacher, Student

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            model_data = form.save(commit=False)
            model_data.role = 'admin'
            model_data.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homeschool',user.id)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def loginview(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            if(SchoolAdmin.objects.filter(user_ptr_id=user.id).count()):
                return redirect('homeschool', user.id)
            if(Teacher.objects.filter(user_ptr_id=user.id).count()):
                return redirect('hometeacher', user.id)
            if(Student.objects.filter(user_ptr_id=user.id).count()):
                return redirect('homestudent', user.id)
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        django_logout(request)
        return redirect('schoolsignup')
