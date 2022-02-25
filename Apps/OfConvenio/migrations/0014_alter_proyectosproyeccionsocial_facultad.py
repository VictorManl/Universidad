# Generated by Django 4.0.2 on 2022-02-17 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OfConvenio', '0013_alter_proyectosproyeccionsocial_facultad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectosproyeccionsocial',
            name='facultad',
            field=models.CharField(choices=[('No aplica', 'No aplica'), ('Facultad de ciencias humanas y artes', 'Facultad de ciencias humanas y artes'), ('Facultad de ciencias de la educacion', 'Facultad de ciencias de la educacion'), ('Facultad de medicina veterinaria', 'Facultad de medicina veterinaria'), ('Facultad de ciencias basicas', 'Facultad de ciencias basicas'), ('Facultad de tecnologia', 'Facultad de tecnologia'), ('IDEAD', 'IDEAD'), ('Facultad de ingenieria agronomica', 'Facultad de ingenieria agronomica'), ('Facultad de ingenieria forestal', 'Facultad de ingenieria forestal'), ('Facultad de ciencias en la salud', 'Facultad de ciencias en la salud')], default='Nn', max_length=80, verbose_name='Facultad'),
        ),
    ]