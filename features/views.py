from django.http.response import Http404
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    html = '<h1>The Features are updated</h1>'

    return HttpResponse(html)
