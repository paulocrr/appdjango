from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from django.template import loader
from django.shortcuts import render

# Create your views here.
def main(request):
	template = loader.get_template('main.html')
	context = {}
	return HttpResponse(template.render(context,request))

def horario(request):
	template = loader.get_template('horario.html')
	context = {}
	return HttpResponse(template.render(context,request))

def calc_notas(request):
	template = loader.get_template('calc_notas.html')
	context = {}
	return HttpResponse(template.render(context,request))

def profesores(request):
	template = loader.get_template('profesores.html')
	context = {}
	return HttpResponse(template.render(context,request))
