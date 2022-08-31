from django.urls import path
from .views import *

app_name = "cart"
urlpatterns = [
    path("", MyCartView.as_view(), name="mycart"),
    path("add-to-cart-<int:product_id>/", AddToCartView.as_view(), name="addtocart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
]