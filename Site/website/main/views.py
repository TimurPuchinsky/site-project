from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>test</h4>")

def about(request):
    return HttpResponse("<h4>test 2</h4>")