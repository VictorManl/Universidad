# Generated by Django 4.0.2 on 2022-03-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('pers_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('pers_documentoidentidad', models.CharField(max_length=50)),
                ('pers_primernombre', models.CharField(max_length=50)),
                ('pers_segundonombre', models.CharField(blank=True, max_length=50, null=True)),
                ('pers_primerapellido', models.CharField(max_length=50)),
                ('pers_segundoapellido', models.CharField(blank=True, max_length=50, null=True)),
                ('pers_sexo', models.CharField(max_length=1)),
                ('pers_rh', models.CharField(max_length=3)),
                ('pers_direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('pers_telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('pers_celular', models.CharField(blank=True, max_length=20, null=True)),
                ('pers_correo', models.CharField(blank=True, max_length=50, null=True)),
                ('pers_correoinstitucional', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': '"GLOBAL"."PERSONA"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('tdoc_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tdoc_nombre', models.CharField(max_length=30)),
                ('tdoc_abreviatura', models.CharField(max_length=5)),
                ('tdoc_tipo', models.CharField(max_length=30)),
                ('tdoc_estado', models.IntegerField()),
            ],
            options={
                'db_table': '"GLOBAL"."tipodocumento"',
                'managed': False,
            },
        ),
    ]
