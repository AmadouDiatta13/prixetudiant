from django.shortcuts import render
from django.views.generic import TemplateView

from products.models import Category, Marque

def HomePageView(request):
    marques = Marque.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'marques': marques, 'categories': categories})

    
class LoginPageView(TemplateView):
    template_name = 'login.html'
    
class ThankPageView(TemplateView):
    template_name = 'thank.html'
    
class InvalideformPageView(TemplateView):
    template_name = 'invalideform.html'