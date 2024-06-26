from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
	path('', include('pages.urls')),
	path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home')

    
]