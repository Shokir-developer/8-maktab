from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='Login_Form')
def sinf1(request):
	pupils = Sinf_1.objects.all()
	context = {'pupils':pupils}
	return render(request, 'sinf/sinf1.html', context)
	
def sinf_1_Id(request, pk):
	pupil = Sinf_1.objects.get(id=pk)
	context = {'pupil':pupil}
	return render(request, 'pupil/pupils_1.html', context)

def sinf2(request):
	pupils = Sinf_2.objects.all()
	context = {'pupils':pupils}
	return render(request, 'sinf/sinf2.html', context)
def sinf_2_Id(request, pk):
	pupil = Sinf_2.objects.get(id=pk)
	context = {'pupil':pupil}
	return render(request, 'pupil/pupils_2.html', context)


def sinf3(request):
	pupils = Sinf_3.objects.all()
	context = {'pupils':pupils}
	return render(request, 'sinf/sinf3.html', context)
def sinf_3_Id(request, pk):
	pupil = Sinf_3.objects.get(id=pk)
	context = {'pupil':pupil}
	return render(request, 'pupil/pupils_3.html', context)

def sinf4(request):
	pupils = Sinf_4.objects.all()
	context = {'pupils':pupils}
	return render(request, 'sinf/sinf4.html', context)
def sinf_4_Id(request, pk):
	pupil = Sinf_4.objects.get(id=pk)
	context = {'pupil':pupil}
	return render(request, 'pupil/pupils_4.html', context)

def sinf5(request):
	pupils = Sinf_5.objects.all()
	context = {'pupils':pupils}
	return render(request, 'sinf/sinf5.html', context)
def sinf_5_Id(request, pk):
	pupil = Sinf_5.objects.get(id=pk)
	context = {'pupil':pupil}
	return render(request, 'pupil/pupils_5.html', context)

def sinf6(request):
	pupils = Sinf_6.objects.all()
	context = {'pupils':pupils}
	return render(request, 'sinf/sinf6.html', context)
def sinf_6_Id(request, pk):
	pupil = Sinf_6.objects.get(id=pk)
	context = {'pupil':pupil}
	return render(request, 'pupil/pupils_6.html', context)

def sinf7(request):
	pupils = Sinf_7.objects.all()
	context = {'pupils':pupils}
	return render(request, 'sinf/sinf7.html', context)
def sinf_7_Id(request, pk):
	pupil = Sinf_7.objects.get(id=pk)
	context = {'pupil':pupil}
	return render(request, 'pupil/pupils_7.html', context)

def sinf8(request):
	pupils = Sinf_8.objects.all()
	context = {'pupils':pupils}
	return render(request, 'sinf/sinf8.html', context)
def sinf_8_Id(request, pk):
	pupil = Sinf_8.objects.get(id=pk)
	context = {'pupil':pupil}
	return render(request, 'pupil/pupils_8.html', context)

def sinf9(request):
	pupils = Sinf_9.objects.all()
	context = {'pupils':pupils}
	return render(request, 'sinf/sinf9.html', context)
def sinf_9_Id(request, pk):
	pupil = Sinf_9.objects.get(id=pk)
	context = {'pupil':pupil}
	return render(request, 'pupil/pupils_9.html', context)

def sinf10(request):
	pupils = Sinf_10.objects.all()
	context = {'pupils':pupils}
	return render(request, 'sinf/sinf10.html', context)
def sinf_10_Id(request, pk):
	pupil = Sinf_10.objects.get(id=pk)
	context = {'pupil':pupil}
	return render(request, 'pupil/pupils_10.html', context)

def sinf11(request):
	pupils = Sinf_11.objects.all()
	context = {'pupils':pupils}
	return render(request, 'sinf/sinf11.html', context)
def sinf_11_Id(request, pk):
	pupil = Sinf_11.objects.get(id=pk)
	context = {'pupil':pupil}
	return render(request, 'pupil/pupils_11.html', context)