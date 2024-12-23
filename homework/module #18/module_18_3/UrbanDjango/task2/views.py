from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class FuncRepresent(TemplateView):
    template_name = 'second_task/first.html'


class ClassRepresent(TemplateView):
    template_name = 'second_task/second.html'
