from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Welcome(TemplateView):
    template_name = 'third_task/welcome.html'


class MainPage(TemplateView):
    template_name = 'third_task/main_page.html'


class Games(TemplateView):
    template_name = 'third_task/games.html'


class Cart(TemplateView):
    template_name = 'third_task/cart.html'
