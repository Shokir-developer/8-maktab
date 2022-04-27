from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

		widgets = {
		'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'username'}),
		'email': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'email'}),
		'password1': forms.PasswordInput(attrs={'class':'form-control'}),
		'password2': forms.PasswordInput(attrs={'class':'form-control'}),

		}