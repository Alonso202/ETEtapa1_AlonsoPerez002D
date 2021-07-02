# Generated by Django 3.2.4 on 2021-06-30 21:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroundZero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='NombreCompleto',
            field=models.CharField(max_length=30, validators=[django.core.validators.MaxValueValidator(999999999)], verbose_name='Nombre del Proveedor'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='Telefono',
            field=models.PositiveIntegerField(verbose_name='Numero Telefonico'),
        ),
    ]