# Generated by Django 4.1.3 on 2022-11-13 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cubicoprojectapp', '0004_alter_galeria_proyectos_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria_proyectos',
            name='descripcion',
            field=models.CharField(max_length=500, verbose_name='descripción general'),
        ),
        migrations.AlterField(
            model_name='galeria_proyectos',
            name='imagen',
            field=models.ImageField(upload_to='', verbose_name='Imagen del proyecto'),
        ),
        migrations.AlterField(
            model_name='galeria_proyectos',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre del proyecto'),
        ),
    ]
