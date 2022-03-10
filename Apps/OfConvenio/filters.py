import django_filters
from Apps.Academico.models import Persona

class filtar_docente(django_filters.FilterSet):
    class Meta:
        model = Persona
        field = 'pers_documentoidentidad'
        exclude = {
            'pers_primernombre',
            'pers_segundonombre',
            'pers_primerapellido',
            'pers_segundoapellido',
            'pers_sexo',
            'pers_rh',
            'pers_direccion',
            'pers_telefono',
            'pers_celular',
            'pers_correo',
            'pers_correoinstitucional',
        }