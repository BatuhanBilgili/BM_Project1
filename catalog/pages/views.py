from django.shortcuts import render
from django.http import HttpRequest
# modelleri çekmek için ekleme yapıyoruz
from .models import *

def index(request):
	# maç ile alakalı verileri çekmek için
	matches = Match.objects.all().order_by('-status')
	return render(request, 'pages/index.html', {'matches': matches})

def about(request):
	return render(request, 'pages/iletisim.html')

def uyeol(request):
	return render(request, "pages/uye-ol.html")

def girisyap(request):
	return render(request, "pages/giris-yap.html")
