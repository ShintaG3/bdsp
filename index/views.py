from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render(request, 'index/index.html')

def organization (request):
    return render(request, 'index/organization.html')

def service (request):
    return render(request, 'index/service.html')

def detail (request):
    return render(request, 'index/detail.html')
