# Generated by Django 4.1.3 on 2022-11-23 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cubico_dato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, verbose_name='Activo o inactivo')),
                ('correo', models.EmailField(max_length=50, verbose_name='Correo electrónico')),
                ('telefono', models.BigIntegerField(verbose_name='Teléfono')),
            ],
        ),
    ]
