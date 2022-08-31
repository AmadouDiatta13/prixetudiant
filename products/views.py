from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView

from cart.views import EcomMixin
from .models import Product, Category, Marque

class ProductsPageView(ListView):
    model = Product
    template_name = "products.html"

def CategoryPageView(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'categories.html', {'products': products})

def MarquePageView(request, marque_id):
    marque = get_object_or_404(Marque, pk=marque_id)
    products = Product.objects.filter(marque=marque)
    return render(request, 'categories.html', {'products': products})  
    
def CartPageView(request):
    return

class ProductDetailView(EcomMixin, TemplateView):
    template_name = "productdetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['product_id']
        product = Product.objects.get(pk=product_id)
        product.view_count += 1
        product.save()
        context['product'] = product
        return context
