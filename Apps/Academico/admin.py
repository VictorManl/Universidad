from atexit import register
from django.contrib import admin
from .models import TipoDocumento,Persona
# Register your models here.

admin.site.register(TipoDocumento)
admin.site,register(Persona)