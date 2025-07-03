from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
# Create your views here.
class HomeView(TemplateView):
    template_name='core/base.html'
from django.views.generic import TemplateView
# Create your views here.

class HomeeView(TemplateView):
    template_name = 'core/index.html'