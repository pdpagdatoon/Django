from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.shortcuts import render
from .utils import handle_comment_section

        
def home(request): # when you want to make a page with comments, copy this function but change the names
    comment_form, comments = handle_comment_section(request)
    return render(request, "hello/home.html", { 
        "comment_form": comment_form,
        "comments": comments,
    })