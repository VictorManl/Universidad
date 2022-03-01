from django.db import models

class TipoDocumento(models.Model):
    tdoc_id = models.BigAutoField(primary_key=True)
    tdoc_nombre = models.CharField(max_length=30)
    tdoc_abreviatura = models.CharField(max_length=5)
    tdoc_tipo = models.CharField(max_length=30)
    tdoc_estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = '"GLOBAL"."tipodocumento"'

class Persona(models.Model):
    pers_id = models.BigAutoField(primary_key=True)
    pers_documentoidentidad = models.CharField(max_length=50)
    pers_primernombre = models.CharField(max_length=50)
    pers_segundonombre = models.CharField(max_length=50,null=True,blank=True)
    pers_primerapellido = models.CharField(max_length=50)
    pers_segundoapellido = models.CharField(max_length=50,null=True,blank=True)
    pers_sexo = models.CharField(max_length=1)
    pers_rh = models.CharField(max_length=3)
    pers_direccion = models.CharField(max_length=100,null=True,blank=True)
    pers_telefono = models.CharField(max_length=20,null=True,blank=True)
    pers_celular = models.CharField(max_length=20,null=True,blank=True)
    pers_correo = models.CharField(max_length=50,null=True,blank=True)
    pers_correoinstitucional = models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        managed = False
        db_table = '"GLOBAL"."PERSONA"'


class PersonaGeneral(models.Model):
    pege_id = models.BigAutoField(primary_key=True)
    pege_tipopersona = models.IntegerField(null=True,blank=True)
    pege_direccion = models.CharField(max_length=100,null=True,blank=True)
    pege_mail = models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        managed = False
        db_table = '"general"."personageneral"'
        
