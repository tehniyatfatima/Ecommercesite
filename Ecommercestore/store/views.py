from django.shortcuts import render

from django.http import HttpResponse

## test function
def test(request):
    return HttpResponse(" store app is connected")


