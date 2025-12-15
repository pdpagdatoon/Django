from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product
from .utils import handle_comment_section
from django.shortcuts import redirect
from .forms import FeedbackForm


def home(request):
    products = Product.objects.all().order_by("group", "title")
    return render(
        request,
        "hello/home.html",
        {
            "products": products,
            "show_comments": False,
        },
    )


# part of generating a page when adding a product through admin
class ProductDetailView(DetailView):
    model = Product
    template_name = "hello/product_detail.html"
    context_object_name = "product"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        handle_comment_section(request)
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form, comments = handle_comment_section(self.request)
        context["comment_form"] = comment_form
        context["comments"] = comments
        context["show_comments"] = True
        return context


def audiomixer_page(request):
    comment_form, comments = handle_comment_section(request)
    products = Product.objects.all().order_by("group", "title")
    return render(
        request,
        "hello/audiomixer.html",
        {
            "products": products,
            "show_comments": True,
            "comment_form": comment_form,
            "comments": comments,
        },
    )


def earbuds_page(request):
    comment_form, comments = handle_comment_section(request)
    products = Product.objects.all().order_by("group", "title")
    return render(
        request,
        "hello/earbuds.html",
        {
            "products": products,
            "show_comments": True,
            "comment_form": comment_form,
            "comments": comments,
        },
    )


def jackcable_page(request):
    comment_form, comments = handle_comment_section(request)
    products = Product.objects.all().order_by("group", "title")
    return render(
        request,
        "hello/jackcable.html",
        {
            "products": products,
            "show_comments": True,
            "comment_form": comment_form,
            "comments": comments,
        },
    )


def compacteddisc_page(request):
    comment_form, comments = handle_comment_section(request)
    products = Product.objects.all().order_by("group", "title")
    return render(
        request,
        "hello/CompactedDisc.html",
        {
            "products": products,
            "show_comments": True,
            "comment_form": comment_form,
            "comments": comments,
        },
    )


def cdplayer_page(request):
    comment_form, comments = handle_comment_section(request)
    products = Product.objects.all().order_by("group", "title")
    return render(
        request,
        "hello/CDplayer.html",
        {
            "products": products,
            "show_comments": True,
            "comment_form": comment_form,
            "comments": comments,
        },
    )


def drums_page(request):
    comment_form, comments = handle_comment_section(request)
    products = Product.objects.all().order_by("group", "title")
    return render(
        request,
        "hello/drums.html",
        {
            "products": products,
            "show_comments": True,
            "comment_form": comment_form,
            "comments": comments,
        },
    )


def guitar_page(request):
    comment_form, comments = handle_comment_section(request)
    products = Product.objects.all().order_by("group", "title")
    return render(
        request,
        "hello/guitar.html",
        {
            "products": products,
            "show_comments": True,
            "comment_form": comment_form,
            "comments": comments,
        },
    )


def piano_page(request):
    comment_form, comments = handle_comment_section(request)
    products = Product.objects.all().order_by("group", "title")
    return render(
        request,
        "hello/piano.html",
        {
            "products": products,
            "show_comments": True,
            "comment_form": comment_form,
            "comments": comments,
        },
    )


from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_thanks')
    else:
        form = FeedbackForm()

    return render(request, 'hello/feedback.html', {'form': form})


def feedback_thanks(request):
    return render(request, 'hello/thanks.html')