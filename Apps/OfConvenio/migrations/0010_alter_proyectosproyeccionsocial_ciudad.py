# Generated by Django 4.0.2 on 2022-02-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OfConvenio', '0009_remove_proyectosproyeccionsocial_totalestudiantes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectosproyeccionsocial',
            name='ciudad',
            field=models.CharField(choices=[('-', '-'), ('Arauca', 'Arauca'), ('Amazonas', 'Leticia')], max_length=30, verbose_name='Ciudad'),
        ),
    ]
