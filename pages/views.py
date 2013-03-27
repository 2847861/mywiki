# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from pages.models import Page, Navig, Cont, Img, Sect

def Home(request):
  p = Page.objects.get(pk = 1)
  n = Navig.objects.get(pk = 1)  
  template = loader.get_template('pages/home.html')
  context = Context({
    'page': p,
	'nav': n,

  })
  return HttpResponse(template.render(context))   
	
def article1(request):
  p = Page.objects.get(pk = 2)
  n = Navig.objects.get(pk = 2) 
  c = Cont.objects.get(pk = 1)
  template = loader.get_template('pages/history.html')
  context = Context({
    'page': p,
	'nav': n,
	'cont': c,

  })
  return HttpResponse(template.render(context))
	
def article2(request):
  p = Page.objects.get(pk = 3)
  n = Navig.objects.get(pk = 3) 
  c = Cont.objects.get(pk = 2)
  i = Img.objects.get(pk = 1)
  s = Sect.objects.get(pk = 1)   
  template = loader.get_template('pages/health.html')
  context = Context({
    'page': p,
	'nav': n,
	'cont': c,
	'img':i,
	'sect':s,
  })
  return HttpResponse(template.render(context))
	
def article3(request):
  p = Page.objects.get(pk = 4)
  n = Navig.objects.get(pk = 4) 
  c = Cont.objects.get(pk = 3)
  i = Img.objects.get(pk = 2)
  s = Sect.objects.get(pk = 2)   
  template = loader.get_template('pages/characteristics.html')
  context = Context({
    'page': p,
	'nav': n,
	'cont': c,
	'img':i,
	'sect':s,
  })
  return HttpResponse(template.render(context))
	


