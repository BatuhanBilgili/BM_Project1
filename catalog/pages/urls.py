from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name="index"),
	path('iletisim.html', views.about, name="about"),
	path("uye-ol.html", views.uyeol, name="uyeol"),
	path("giris-yap.html", views.girisyap, name="girisyap")
]