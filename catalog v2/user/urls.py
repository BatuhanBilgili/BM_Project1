from django.urls import path
from . import views


urlpatterns = [
	path('login/giris-yap.html', views.login, name='login'),
	path('register/uye-ol.html', views.register, name='register'),
	# path('logout/', views.logout, name='logout')
]