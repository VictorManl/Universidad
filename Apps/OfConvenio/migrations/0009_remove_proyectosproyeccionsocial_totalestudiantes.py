# Generated by Django 4.0.2 on 2022-02-16 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OfConvenio', '0008_proyectosproyeccionsocial_totalestudiantes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyectosproyeccionsocial',
            name='totalEstudiantes',
        ),
    ]