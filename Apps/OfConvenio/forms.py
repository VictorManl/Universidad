from django import forms
from django.forms.utils import ErrorList

from .models import Convenios, ProyectosProyeccionSocial
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class listaFormulario(forms.ModelForm):
    class Meta:
        model = Convenios
        field = [
            'convenio',
            'documento',
            'nombre',
            'telefono',
            'municipio',
            'programa',
            'facultad',
        ]
        exclude = [
            'codigo',
            'fecha',
        ]
        labels = { 
            'convenio' : 'Numero del convenio',
            'documento' : 'Documento de identidad',
            'nombre' : 'Nombre',
            'telefono' : 'Numero telefonico',
            'municipio' : 'Ciudad o municipio',
            'programa' : 'Nombre del programa',
            'facultad' : 'Facultad',
        }
        help_texts = { 
            'convenio' : 'Ingrese el numero del convenio',
            'documento' : 'Ingrese el documento de identidad',
            'nombre' : 'Ingrese el nombre',
            'telefono' : 'Ingrese el numero telefonico',
            'municipio' : 'Ingrese el nombre de la ciudad o municipio',
            'programa' : 'Ingrese el nombre del programa',
            'facultad' : 'Ingrese el nombre de la facultad',
        }

class formC(forms.ModelForm):
    class Meta:
        model = ProyectosProyeccionSocial
        field = [
            'programa',
            'ciudad',
            'institucion',
            'numeroEstudiantes',
            'tipoComunidad',
            'organizacion',
            'facultad',
            'nombreProyecto',
            'codigoBput',
            'descripcion',
            'evidencia'
        ]
        labels = {
            'programa': 'Nombre del programa',
            'ciudad': 'Ciudad / Municipio',
            'institucion':'Nombre de la institucion',
            'numeroEstudiantes': 'Numero de estudiantes',
            'tipoComunidad': 'Tipo de comunidad',
            'organizacion': 'Organizacion',
            'facultad': 'Facultad',
            'nombreProyecto': 'Nombre del proyecto',
            'nombreDocente': 'Nombre del docente',
            'codigoBput': 'Codigo BPUT',
            'descripcion': 'Descripcion',
        }
        exclude = [
            'codigo',
            'fecha',
            'nombreDocente',

        ]
        

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}
        
