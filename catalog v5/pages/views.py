from django.shortcuts import render
from django.http import HttpRequest
# modelleri çekmek için ekleme yapıyoruz
from .models import *

def index(request):
	# maç ile alakalı verileri çekmek için
	matches = Match.objects.all().order_by('-status')
	table = LeagueTable.objects.all().order_by('-points')
	return render(request, 'pages/index.html', {'matches': matches, 'table': table})

def about(request):
	return render(request, 'pages/iletisim.html')

