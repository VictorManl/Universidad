from re import T
from django.db import models
from Apps.Academico.models import Persona,TipoDocumento,IntegranteProyecto



# Create your models here.

class Ciudad(models.Model):
    ciud_id = models.BigAutoField(primary_key=True)
    ciud_nombre = models.CharField(max_length=50,null=True,blank=True)
    ciud_codigodian = models.CharField(max_length=5,null=True,blank=True)


    class Meta:
        managed = False
        db_table = '"GLOBAL"."CIUDAD"'
        
class Programas(models.Model):
    prog_id = models.AutoField('Id',primary_key=True)
    prog_programa = models.CharField('Programa',max_length=50,null=True,blank=True)
    
    class Meta:
        managed = False
        verbose_name_plural = "Programas"
        db_table = '"PROYECCIONSOCIAL"."PROGRAMA"'
    

class Convenios(models.Model):
    conv_id = models.AutoField('Id', primary_key=True, blank=False) 
    conv_fecha = models.DateField('Fecha',max_length=15, auto_now_add=True)
    conv_documento = models.CharField('Documento', max_length=15, null= False, blank=False)
    conv_numeroconvenio = models.CharField('Numero Convenio', max_length=20, null=False, blank=False)
    conv_nombreconvenio = models.CharField('Nombre Convenio', max_length= 80, null= False, blank=False)
    conv_nombreestudiante = models.CharField('Nombre Estudiante', max_length=80, null= False, blank=False)
    conv_telefono = models.CharField('Telefono', max_length=80,null=False,blank=False)
    ciud_id = models.ForeignKey(Ciudad, on_delete=models.CASCADE,db_column='ciud_id')
    prog_id = models.ForeignKey(Programas,on_delete=models.CASCADE,db_column='prog_id')


    class Meta:
        managed = False
        verbose_name_plural = "Convenios"
        db_table = '"PROYECCIONSOCIAL"."CONVENIOS"'
    
    def __str__(self):
                texto = "{0} {1} {2} {3}"
                return texto.format(self.conv_fecha,self.conv_documento,self.conv_numeroconvenio,self.conv_nombreconvenio)


class Comunidad(models.Model):
    comu_id = models.AutoField('Id',primary_key=True,blank=False)
    comu_nombrecomunidad = models.CharField('Nombre comuniad', max_length=100,null=True,blank=True)
    comu_codigo = models.CharField('Codigo', max_length= 100,null=True,blank=True)
    
    class Meta:
        manage = False
        verbose_name_plural = "Comunidades"
        db_table = '"PROYECCIONSOCIAL"."COMUNIDAD'
        


class Proyectos(models.Model):
    proy_id = models.AutoField('Id',primary_key=True,blank=True)
    proy_fecha = models.DateField('Fecha',max_length=15, auto_now_add=True)    
    prog_id = models.ForeignKey(Programas,on_delete=models.CASCADE,db_column='prog_id')
    comu_id = models.ForeignKey(Comunidad,on_delete=models.CASCADE,db_column='comu_id')
    pers_id = models.ForeignKey(Persona,on_delete=models.CASCADE,db_column='pers_id')
    conv_id = models.ForeignKey(Convenios,on_delete=models.CASCADE,db_column='conv_id')
    cuid_id = models.ForeignKey(Ciudad,on_delete=models.CASCADE,db_column='cuid_id')
    inpo_id = models.ForeignKey(IntegranteProyecto,on_delete=models.CASCADE,db_column='inpo_id')
    tdoc_id = models.ForeignKey(TipoDocumento,on_delete=models.CASCADE,db_column='tdoc_id')
    proy_subproyecto = models.CharField('Subproyecto',max_length=100,null=True,blank=True)
    proy_numeroestudiantes = models.CharField('Numero de estudiantes',max_length=100,null=True,blank=True)
    proy_nombreinstitucion = models.CharField('Nombre Institucion',max_length=100,null=True,blank=True)
    proy_codigobput = models.CharField('Codigo Bput',max_length=100,null=True,blank=True)
    proy_evidencia = models.CharField('Evidencia',max_length=100,null=True,blank=True)
    proy_organizacion = models.CharField('Organiziacion',max_length=100,null=True,blank=True)
    proy_decripcion = models.CharField('Descripcion',max_length=100,null=True,blank=True)  
    
    class Meta:
        manage = False
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        db_table = '"PROYECCIONSOCIAL"."PROYECTOS"'
        
    def __str__(self):
        texto = "{0} {1} {2} {3}"
        return texto.format(self.proy_fecha,self.proy_id,self.prog_id,self.proy_subproyecto)




