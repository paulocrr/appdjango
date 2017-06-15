from django import forms

class RegistroForm(forms.Form):
    nombres = forms.CharField(max_length=30)
    #apellidoPaterno = forms.CharField(max_length=30)
    apellidoMaterno = forms.CharField(max_length=30)
    carrera = forms.IntegerField()
    email = forms.CharField(max_length=40)
    secso = forms.CharField(max_length=1)
