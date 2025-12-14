from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.shortcuts import render
from .utils import handle_comment_section
from django.views.generic import DetailView
from .models import Product
        
def home(request): # when you want to make a page with comments, copy this function but change the names
    comment_form, comments = handle_comment_section(request)
    return render(request, "hello/home.html", { 
        "comment_form": comment_form,
        "comments": comments,
    }) 

# part of generating a page when adding a product through admin
class ProductDetailView(DetailView):
    model = Product
    template_name = "hello/product_detail.html"
    context_object_name = "product"