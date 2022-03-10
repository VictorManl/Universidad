from django import forms
from .models import Convenios,Proyectos
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class listaFormulario(forms.ModelForm):
    class Meta:
        model = Convenios
        field = [
            'conv_numeroconvenio',
            'conv_documento',
            'conv_nombreconvenio',
            'conv_nombreestudiante',
            'conv_telefono',
            'ciud_id',
            'prog_id',
        ]
        exclude = [
            'conv_id',
            'conv_fecha',
        ]
        labels = { 
            'conv_numeroconvenio' : 'Numero del convenio',
            'conv_nombreconvenio':'Nombre del convenio',
            'conv_documento' : 'Documento de identidad',
            'conv_nombreestudiante' : 'Nombre estudiante',
            'conv_telefono' : 'Numero telefonico',
            'ciud_id' : 'Ciudad o municipio',
            'prog_id' : 'Nombre del programa',
        }
        help_texts = { 
            'conv_numeroconvenio' : 'Ingrese el numero del convenio',
            'conv_nombreconvenio':'Nombre del convenio',
            'conv_documento' : 'Ingrese el documento de identidad',
            'conv_nombreestudiante' : 'Ingrese el nombre',
            'conv_telefono' : 'Ingrese el numero telefonico',
            'ciud_id' : 'Ingrese el nombre de la ciudad o municipio',
            'prog_id' : 'Ingrese el nombre del programa',
        }

class formC(forms.ModelForm):
    class Meta:
        model = Proyectos
        field = [
            'prog_id',
            'proy_subproyecto',
            'cuid_id',
            'proy_nombreinstitucion',
            'proy_numeroestudiantes',
            'comu_id',
            'proy_organizacion',
            'facultad',
            'nombreProyecto',
            'codigoBput',
            'descripcion',
            'evidencia'
        ]
        labels = {
            'prog_id': 'Nombre del programa',
            'proy_subproyecto' : 'Sub Proyecto',
            'cuid_id': 'Ciudad / Municipio',
            'proy_nombreinstitucion':'Nombre de la institucion',
            'proy_numeroestudiantes': 'Numero de estudiantes',
            'comu_id': 'Tipo de comunidad',
            'proy_organizacion': 'Organizacion',
            'facultad': 'Facultad',
            'nombreProyecto': 'Nombre del proyecto',
            'nombreDocente': 'Nombre del docente',
            'codigoBput': 'Codigo BPUT',
            'descripcion': 'Descripcion',
        }
        exclude = [
            'proy_id',
            'proy_fecha',
        ]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}
        

