from django.urls import path
from .views import index, rahbariyat, contact, newId, registerForm, LoginForm, logoutPage

urlpatterns = [
	path('', index, name='home'),
	path('news/<str:pk>/', newId, name='newId'),
	path('rahbariyat/', rahbariyat, name='rahbariyat'),
	path('contact/', contact, name='contact'),
	path('register/', registerForm, name='register_form'),
	path('login/', LoginForm, name='Login_Form'),
	path('logout/', logoutPage, name='logout_page'),
]