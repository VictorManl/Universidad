# Generated by Django 4.0.2 on 2022-02-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OfConvenio', '0006_alter_proyectosproyeccionsocial_codigobput_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectosproyeccionsocial',
            name='numeroEstudiantes',
            field=models.IntegerField(default=0, verbose_name='Numero de estudiantes'),
        ),
    ]