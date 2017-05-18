from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^main/$', views.main, name="main"),
	url(r'^horario/$', views.horario, name="horario"),
	url(r'^calc_notas/$', views.calc_notas, name="calc_notas"),
	url(r'^profesores/$', views.profesores, name="profesores")
]
