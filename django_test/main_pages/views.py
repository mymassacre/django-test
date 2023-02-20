from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    date = {
        'title': 'Главная страница'
    }
    return render(request, 'main_pages/index.html', date)


def about(request):
    return render(request, 'main_pages/about.html')
