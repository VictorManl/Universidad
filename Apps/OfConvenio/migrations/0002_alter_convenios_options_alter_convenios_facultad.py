# Generated by Django 4.0.2 on 2022-02-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OfConvenio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='convenios',
            options={'verbose_name_plural': 'Convenios'},
        ),
        migrations.AlterField(
            model_name='convenios',
            name='facultad',
            field=models.CharField(choices=[('Facultad de ciencias humanas y artes', 'Facultad de ciencias humanas y artes'), ('Facultadda de ciencias de la educacion', 'Facultadda de ciencias de la educacion'), ('Facultad de medicina veterinaria', 'Facultad de medicina veterinaria'), ('Facultada de ciencias basicas', 'Facultada de ciencias basicas'), ('Facultad de tecnologia', 'Facultad de tecnologia'), ('IDEAD', 'IDEAD'), ('Facultad de ingenieria agronomica', 'Facultad de ingenieria agronomica'), ('Facultad de ingenieria forestal', 'Facultad de ingenieria forestal'), ('Facultad de ciencias en la salud', 'Facultad de ciencias en la salud')], max_length=80, verbose_name='Facultad'),
        ),
    ]