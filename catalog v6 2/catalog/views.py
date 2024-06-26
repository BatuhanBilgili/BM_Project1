from django.shortcuts import render
# from api import fetch_matches  # api.py dosyasını root seviyesinden import ediyoruz

def home(request):
    # matches = fetch_matches()
    return render(request, 'pages/index.html', {'matches': matches})
