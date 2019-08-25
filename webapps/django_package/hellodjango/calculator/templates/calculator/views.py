from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def add(request, x, y):
    return HttpResponse(x + y)


def sub(request, x, y):
    return HttpResponse(x - y)


def mul(request, x, y):
    return HttpResponse(x * y)


def div(request, x, y):
    return HttpResponse(x / y)
