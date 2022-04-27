from django.urls import path
from .views import *

urlpatterns = [
	path('1_sinf', sinf1, name='sinf1'),
	path('1_sinf/<str:pk>/', sinf_1_Id, name='sinf_1_Id'),

	path('2_sinf', sinf2, name='sinf2'),
	path('2_sinf/<str:pk>/', sinf_2_Id, name='sinf_2_Id'),

	path('3_sinf', sinf3, name='sinf3'),
	path('3_sinf/<str:pk>/', sinf_3_Id, name='sinf_3_Id'),

	path('4_sinf', sinf4, name='sinf4'),
	path('4_sinf/<str:pk>/', sinf_4_Id, name='sinf_4_Id'),

	path('5_sinf', sinf5, name='sinf5'),
	path('5_sinf/<str:pk>/', sinf_5_Id, name='sinf_5_Id'),

	path('6_sinf', sinf6, name='sinf6'),
	path('6_sinf/<str:pk>/', sinf_6_Id, name='sinf_6_Id'),

	path('7_sinf', sinf7, name='sinf7'),
	path('7_sinf/<str:pk>/', sinf_7_Id, name='sinf_7_Id'),

	path('8_sinf', sinf8, name='sinf8'),
	path('8_sinf/<str:pk>/', sinf_8_Id, name='sinf_8_Id'),

	path('9_sinf', sinf9, name='sinf9'),
	path('9_sinf/<str:pk>/', sinf_9_Id, name='sinf_9_Id'),

	path('10_sinf', sinf10, name='sinf10'),
	path('10_sinf/<str:pk>/', sinf_10_Id, name='sinf_10_Id'),

	path('11_sinf', sinf11, name='sinf11'),
	path('11_sinf/<str:pk>/', sinf_11_Id, name='sinf_11_Id'),
]
