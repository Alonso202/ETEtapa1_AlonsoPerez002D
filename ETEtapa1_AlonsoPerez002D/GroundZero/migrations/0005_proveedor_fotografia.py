# Generated by Django 3.1 on 2021-07-04 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroundZero', '0004_auto_20210702_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='Fotografia',
            field=models.ImageField(null=True, upload_to='proveedores'),
        ),
    ]
