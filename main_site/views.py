from django.shortcuts import render
from django.views.generic import TemplateView


class TemplatePrincipal(TemplateView):
    template_name = 'home.html'


class Index(TemplateView):
    template_name = 'index.html'
