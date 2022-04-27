from django.shortcuts import render, redirect
from .models import News
from .forms import CreateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def registerForm(request):
	form  = CreateUserForm()
	if request.method =='POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form}
	return render(request, 'register.html', context)

def LoginForm(request):
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('/')

	return render(request, 'login.html')

def logoutPage(request):
	logout(request)
	return redirect('/')



@login_required(login_url='Login_Form')
def index(request):
	news = News.objects.all()
	context = {'news':news}
	return render(request, 'index.html', context)

@login_required(login_url='Login_Form')
def newId(request, pk):
	news = News.objects.get(id=pk)
	context = {'news':news}
	return render(request, 'news.html', context)

@login_required(login_url='Login_Form')
def rahbariyat(request):
	context = {}
	return render(request, 'rahbariyat.html', context)


@login_required(login_url='Login_Form')
def contact(request):
	context = {}
	return render(request, 'contact.html', context)

