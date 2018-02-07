from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = "home.html"

# def home_view(request):
#     template = 'home.html'
#     context = {}
#     return render(request, template, context)