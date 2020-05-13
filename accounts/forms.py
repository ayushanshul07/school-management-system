from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import SchoolAdmin


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    middle_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    school_name = forms.CharField(max_length=30, required=True, help_text='Enter the school name')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = SchoolAdmin
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'school_name', 'email', 'password1', 'password2', )