# Generated by Django 5.0.6 on 2024-06-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appevaluacion', '0013_remove_detalleevaluacion_coherencia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurado',
            name='dni',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='jurado',
            name='telefono',
            field=models.CharField(max_length=10, null=True),
        ),
    ]