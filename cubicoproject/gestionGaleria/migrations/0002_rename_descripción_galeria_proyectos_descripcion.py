# Generated by Django 4.1.3 on 2022-11-09 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionGaleria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galeria_proyectos',
            old_name='descripción',
            new_name='descripcion',
        ),
    ]
