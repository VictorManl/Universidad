from django.db import models

# Create your models here.

class Convenios(models.Model):
    PROYECTOS_CHOICES = (
        ('Regionalizacion', 'Regionalizacion'),
        ('UT Solidaria', 'UT Solidaria'),
        ('UT Para los niños', 'UT Para los niños'),
        ('UT En tu comunidad', 'UT En tu comunidad'),
        ('Articulacion con la escuela', 'Articulacion con la escuela'),
        ('Universidad territorio de paz', 'Universidad territorio de paz'),
        ('Apropiacion social del conocimiento', 'Apropiacion social del conocimiento'),
        ('Universidad abierta', 'Universidad abierta'),
    )
    FACULTAD_CHOICES = (
        ('No aplica','No aplica'),
        ('Facultad de ciencias humanas y artes','Facultad de ciencias humanas y artes'),
        ('Facultad de ciencias de la educacion','Facultad de ciencias de la educacion'),
        ('Facultad de medicina veterinaria','Facultad de medicina veterinaria'),
        ('Facultad de ciencias basicas','Facultada de ciencias basicas'),
        ('Facultad de tecnologia','Facultad de tecnologia'),
        ('IDEAD','IDEAD'),
        ('Facultad de ingenieria agronomica','Facultad de ingenieria agronomica'),
        ('Facultad de ingenieria forestal','Facultad de ingenieria forestal'),
        ('Facultad de ciencias en la salud','Facultad de ciencias en la salud'),
    )
    
    codigo = models.AutoField('Codigo',primary_key=True,blank=False)
    fecha = models.DateField('Fecha',max_length=15, auto_now_add=True)
    documento = models.CharField('Cc Estudiante',max_length=30, blank=False, null=False)
    convenio = models.CharField('Numero Convenio',max_length=30, blank=False, null=False)
    nombre = models.CharField('Nombre Estudiante',max_length=40, blank=False, null=False)
    telefono = models.CharField('Celular Estudiante',max_length=15, blank=False, null=False)
    municipio = models.CharField('Municipio',max_length=30, blank=False, null=False)
    programa = models.CharField('Programa',max_length= 50, blank=False, null=False, choices=PROYECTOS_CHOICES)
    facultad = models.CharField('Facultad',max_length= 80, null= False, choices= FACULTAD_CHOICES)
    
    class Meta:
        verbose_name_plural = "Convenios"
    
    def __str__(self):
                texto = "{0} ({1}) {2} {3})"
                return texto.format(self.fecha, self.documento, self.nombre,self.convenio)
            
class ProyectosProyeccionSocial(models.Model):
    PROYECTOS_CHOICES = (
        ('Regionalizacion','Regionalizacion'),
        ('UT Solidaria','UT Solidaria'),
        ('UT Para los niños','UT Para los niños'),
        ('UT En tu comunidad','UT En tu comunidad'),
        ('Articulacion con la escuela','Articulacion con la escuela'),
        ('Universidad territorio de paz','Universidad territorio de paz'),
        ('Apropiacion social del conocimiento','Apropiacion social del conocimiento'),
        ('Universidad abierta','Universidad abierta'),
    )
    CIUDADES_CHOICES=(
        ('Ibague','Ibague'),
        ('Bogota','Bogota'),
        
    )
    COMUNIDAD_CHOICES = (
        ('No aplica', 'No aplica'),
        ('Indigena', 'Indigena'),
        ('Afrodecendiente', 'Afrodecendiente'),
        ('Campesino', 'Campesino'),
        ('Comunidad LGBTI', 'Comunidad LGBTI'),
        ('Victima del conflicto armado', 'Victima del conflicto armado'),)
    FACULTAD_CHOICES = (
        ('No aplica', 'No aplica'),
        ('Facultad de ciencias humanas y artes', 'Facultad de ciencias humanas y artes'),
        ('Facultad de ciencias de la educacion', 'Facultad de ciencias de la educacion'),
        ('Facultad de medicina veterinaria', 'Facultad de medicina veterinaria'),
        ('Facultad de ciencias basicas', 'Facultad de ciencias basicas'),
        ('Facultad de tecnologia', 'Facultad de tecnologia'),
        ('IDEAD', 'IDEAD'),
        ('Facultad de ingenieria agronomica', 'Facultad de ingenieria agronomica'),
        ('Facultad de ingenieria forestal', 'Facultad de ingenieria forestal'),
        ('Facultad de ciencias en la salud', 'Facultad de ciencias en la salud'),
    )
    codigo = models.AutoField('Codigo',primary_key=True,blank=False)
    fecha = models.DateField('Fecha',max_length=15, auto_now_add=True)
    programa = models.CharField('Programa',max_length= 50, null=False, choices = PROYECTOS_CHOICES)
    ciudad = models.CharField('Ciudad',max_length=30, blank=False, null=False, choices=CIUDADES_CHOICES)
    institucion = models.CharField('Nombre de la institucion',max_length=30, blank=False, null=False)
    codigoBput = models.CharField('Codigo BPUT', max_length=50, default=0, editable=True)
    evidencia = models.ImageField(upload_to="Evidencias", null=True)
    nombreDocente = models.CharField('Nombre del docente', max_length=50, default='Nn', editable=True)
    numeroEstudiantes = models.IntegerField('Numero de estudiantes', default=0, editable=True)
    tipoComunidad = models.CharField('Tipo de Comunidad', max_length=30, choices=COMUNIDAD_CHOICES, default='Nn',
                                      editable=True)
    organizacion = models.CharField('Organizacion', max_length=30, default='Nn', editable=True)
    facultad = models.CharField('Facultad', max_length=80, choices=FACULTAD_CHOICES, default='Nn', editable=True)
    nombreProyecto = models.CharField('Nombre del proyecto',max_length= 50,default='Nn', editable=True)
    descripcion = models.CharField('Descripcion', max_length= 200, blank=False, null=False)


    def __str__(self):
                texto = "{0} ({1}) {2} {3})"
                return texto.format(self.fecha, self.programa, self.ciudad,self.institucion)
            