# Generated by Django 3.2.4 on 2021-07-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroundZero', '0002_auto_20210630_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='NumeroIden',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Numero Identificación'),
        ),
    ]
