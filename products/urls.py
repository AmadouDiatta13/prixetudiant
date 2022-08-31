from django.urls import path
from . import views
from .views import ProductsPageView, CategoryPageView, MarquePageView, ProductDetailView

app_name = "products"
urlpatterns = [
    path("", ProductsPageView.as_view(), name="products"),
    path('marque/<int:marque_id>/', MarquePageView, name='marques'),
    path('category/<int:category_id>/', CategoryPageView, name='categories'),
    path("<int:product_id>/", ProductDetailView.as_view(), name="productdetail"),
]