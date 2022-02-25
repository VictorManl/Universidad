# Generated by Django 4.0.2 on 2022-02-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convenios',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo')),
                ('fecha', models.DateField(auto_now_add=True, max_length=15, verbose_name='Fecha')),
                ('documento', models.CharField(max_length=30, verbose_name='Cc Estudiante')),
                ('convenio', models.CharField(max_length=30, verbose_name='Numero Convenio')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre Estudiante')),
                ('telefono', models.CharField(max_length=15, verbose_name='Celular Estudiante')),
                ('municipio', models.CharField(max_length=30, verbose_name='Municipio')),
                ('programa', models.CharField(max_length=50, verbose_name='Programa')),
                ('facultad', models.CharField(max_length=50, verbose_name='Facultad')),
            ],
        ),
    ]