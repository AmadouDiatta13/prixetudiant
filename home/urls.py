from django.urls import path
from .views import HomePageView, ThankPageView, InvalideformPageView

app_name = "home"

urlpatterns = [
	path("", HomePageView, name="home"),
    path("thank/", ThankPageView.as_view(), name="thank"),
    path("invalideForm/", InvalideformPageView.as_view(), name="invalideForm"),
]