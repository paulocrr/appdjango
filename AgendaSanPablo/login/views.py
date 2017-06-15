from django.http import HttpResponse,Http404
from django.template import loader
from django.shortcuts import render
from .models import persona
from .forms import RegistroForm

def index(request):
	template = loader.get_template('index.html')
	context = {}
	return HttpResponse(template.render(context,request))

def registration(request):
	p = persona()
	template = loader.get_template('registro.html')
	return HttpResponse(template.render({},request))

# Create your views here.
