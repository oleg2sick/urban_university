from django.shortcuts import render
#from django.views.generic import TemplateView
# Create your views here.


def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'third_task/main_page.html', context)

def game(request):
    context = {
        'title': 'Игры',
        'first': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    }
    return render(request, 'third_task/games.html', context)

def cart(request):
    context = {
        'title': 'Корзина'
    }
    return render(request, 'third_task/cart.html', context)
