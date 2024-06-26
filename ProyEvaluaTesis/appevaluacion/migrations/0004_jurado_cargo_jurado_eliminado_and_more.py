# Generated by Django 5.0.6 on 2024-06-02 16:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appevaluacion', '0003_alumno_ncelular_alter_alumno_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurado',
            name='cargo',
            field=models.CharField(choices=[('Presidente', 'Presidente'), ('Secretario', 'Secretario'), ('Vocal', 'Vocal')], default='Presidente', max_length=20),
        ),
        migrations.AddField(
            model_name='jurado',
            name='eliminado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jurado',
            name='fecha_actualizacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='jurado',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
