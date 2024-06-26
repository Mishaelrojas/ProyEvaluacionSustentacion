# Generated by Django 5.0.6 on 2024-06-03 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appevaluacion', '0012_jurado_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleevaluacion',
            name='Coherencia',
        ),
        migrations.RemoveField(
            model_name='detalleevaluacion',
            name='Dominio_tema',
        ),
        migrations.RemoveField(
            model_name='detalleevaluacion',
            name='Importancia',
        ),
        migrations.RemoveField(
            model_name='detalleevaluacion',
            name='Metodologia',
        ),
        migrations.RemoveField(
            model_name='detalleevaluacion',
            name='Originalidad',
        ),
        migrations.RemoveField(
            model_name='detalleevaluacion',
            name='Validez',
        ),
        migrations.AddField(
            model_name='detalleevaluacion',
            name='coherencia',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.AddField(
            model_name='detalleevaluacion',
            name='dominio_tema',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.AddField(
            model_name='detalleevaluacion',
            name='importancia',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.AddField(
            model_name='detalleevaluacion',
            name='metodologia',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.AddField(
            model_name='detalleevaluacion',
            name='originalidad',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
        migrations.AddField(
            model_name='detalleevaluacion',
            name='validez',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
        ),
    ]
