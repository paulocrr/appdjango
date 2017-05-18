from django.http import HttpResponse,Http404
from django.template import loader
from django.shortcuts import render

def index(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context,request))

def registration(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context,request))

def logout(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context,request))
# Create your views here.


