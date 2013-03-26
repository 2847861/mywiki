# Create your views here.
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from pages.models import Page

def Home(request):
    return render(request, 'pages/home.html')
	
def article1(request):
	return render(request, 'pages/history.html')
	
def article2(request):
	return render(request, 'pages/health.html')
	
def article3(request):
	return render(request, 'pages/characteristics.html')
	


