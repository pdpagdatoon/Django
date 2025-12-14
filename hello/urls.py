from django.urls import path
from hello import views
from hello.views import ProductDetailView

urlpatterns = [
    path("", views.home, name="home"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name= "product-detail"), # to generate a url when adding a product through admin
]
