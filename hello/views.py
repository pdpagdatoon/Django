from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product
from .utils import handle_comment_section

def home(request):
    products = Product.objects.all().order_by("group", "title")
    return render(request, "hello/home.html", {
        "products": products,
        "show_comments": False,
    })


# part of generating a page when adding a product through admin
class ProductDetailView(DetailView):
    model = Product
    template_name = "hello/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form, comments = handle_comment_section(self.request)
        context["comment_form"] = comment_form
        context["comments"] = comments
        context["show_comments"] = True
        return context

