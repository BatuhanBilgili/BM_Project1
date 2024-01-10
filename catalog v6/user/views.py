from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# loginde kullanılacak
from django.contrib import auth
from django.contrib import messages

def login(request):
	#post metodu gerçekleşti öi
	if request.method == "POST":
		#veriler alınıyor
		username = request.POST['username']
		password = request.POST['password']
		#veriler sistemde kayıtlı mı 
		user = auth.authenticate(username=username, password=password)
		#sistemde veri varsa 
		if user is not None:
			#sisteme giriş yapabilir
			auth.login(request, user)
			messages.add_message(request, messages.SUCCESS, 'Oturum açıldı')
			return redirect('index')
		else:
			messages.add_message(request, messages.ERROR, 'Hatalı kullanıcı adı veya şifre')
			return redirect('login')
	else:
		return render(request, 'user/giris-yap.html')

def register(request):
	if request.method == "POST":
		#veriler alındı
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		repassword = request.POST['repassword']
		#parolalar kontrol ediliyor
		if password == repassword:
			#kullanıcı adı kayıtlı mı
			if User.objects.filter(username = username).exists():
				messages.add_message(request, messages.WARNING, 'Bu kullanıcı adı alınmış')
				return redirect('register')
			else:
				#mail adresi kontrol edilir
				if User.objects.filter(email = email).exists():
					messages.add_message(request, messages.WARNING, 'Bu email daha önce kullanılmış')
					return redirect('register')
				else:
					#kayıt işlemi yapılıyor
					user = User.objects.create_user(username=username, email=email, password=password)
					user.save()
					messages.add_message(request, messages.SUCCESS, 'Kullanıcı oluşturuldu')
					return redirect('login')
		else:
			print("!Girilen şifreler eşleşmiyor")
			return redirect('register')	
	else:
		return render(request, 'user/uye-ol.html')



# logout yazılacak
def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		messages.add_message(request, messages.SUCCESS, 'Oturumunuz kapatıldı.')
		return redirect('/')

