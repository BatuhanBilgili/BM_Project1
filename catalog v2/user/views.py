from django.shortcuts import render

def login(request):
	return render(request, 'user/giris-yap.html')

def register(request):
	return render(request, 'user/uye-ol.html')

def about(request):
	return render(request, 'pages/iletisim.html')

# logout yazılacak

