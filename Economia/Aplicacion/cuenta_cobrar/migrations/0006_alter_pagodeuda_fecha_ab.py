# Generated by Django 4.1.1 on 2022-09-22 05:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta_cobrar', '0005_alter_pagodeuda_abono_alter_pagodeuda_fecha_ab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagodeuda',
            name='fecha_ab',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de abono'),
        ),
    ]