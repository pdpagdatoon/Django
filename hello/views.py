from django.shortcuts import render
from django.http import HttpResponse
import datetime


def home(request):
    return render(request, "hello/home.html", {"date": datetime.datetime.now()})


def about(request):
    return render(request, "hello/about.html")


def contact(request):
    return render(
        request,
        "hello/contact.html",
    )


def hello_there(request, name):
    print(request.build_absolute_uri())
    return render(
        request,
        "hello/hello_there.html",
        {"name": name, "date": datetime.datetime.now()},
    )
