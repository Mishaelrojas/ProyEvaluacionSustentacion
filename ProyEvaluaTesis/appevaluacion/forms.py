from django import forms 
from django.forms import fields 
from appevaluacion.models import *
from django.contrib.auth.models import User
import datetime

#-------------------------------------- Formulario para Crear Alumno-------------------------------------
class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = [
            'codigo',
            'nombre_ponente',            
            'dni',
            'email',
            'ncelular',
            'ponencia',
            'doctorado_maestria',
            'unidad',            
            'mencion',
            'sala',            
            'fecha_sustentacion',            
            'hora_inicio_sustentacion',
            'hora_fin_sustentacion',
            'asesor',            
        ]
        widgets = {                            
            'codigo': forms.TextInput(attrs={'placeholder': 'Ingrese codigo'}),
            'nombre_ponente': forms.TextInput(attrs={'placeholder': 'Ingrese nombres y apellidos'}),           
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese dni'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ingrese correo electronico'}),
            'ncelular': forms.TextInput(attrs={'placeholder': 'Ingrese celular'}),
            'ponencia': forms.TextInput(attrs={'placeholder': 'Ingrese titulo de la ponencia'}),
            'doctorado_maestria': forms.TextInput(attrs={'placeholder': 'Ingrese el programa'}),            
            'unidad': forms.TextInput(attrs={'placeholder': 'Ingrese unidad'}),
            'mencion': forms.TextInput(attrs={'placeholder': 'Ingrese mención'}),
            'sala': forms.TextInput(attrs={'placeholder': 'Ingrese sala'}),
            'fecha_sustentacion': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control',
                'placeholder': 'Seleccione una fecha'
            }),
            'hora_inicio_sustentacion': forms.TimeInput(attrs={
                'type': 'time', 
                'class': 'form-control',
                'placeholder': 'Seleccione una hora inicio'
            }),
            'hora_fin_sustentacion': forms.TimeInput(attrs={
                'type': 'time', 
                'class': 'form-control',
                'placeholder': 'Seleccione una hora final'
            }),
        }
        labels = {
            'codigo': 'Codigo',
            'nombre_ponente': 'Nombre ponente',
            'dni': 'Dni',
            'email': 'Email',
            'ncelular': 'Ncelular',
            'ponencia': 'Ponencia',
            'doctorado_maestria': 'Doctorado maestria',
            'unidad': 'Unidad',
            'mencion': 'Mencion',
            'sala': 'Sala',
            'fecha_sustentacion': 'Fecha sustentacion',
            'hora_inicio_sustentacion': 'Hora Inicio',
            'hora_fin_sustentacion': 'Hora Fin',
            'asesor': 'Asesor',
        }


""" class DetalleEvaluacionForm(forms.ModelForm):
    class Meta:
        model = DetalleEvaluacion
        fields = ['Originalidad', 'Importancia', 'Coherencia', 'Metodologia', 'Validez', 'Dominio_tema', 'sugerencias']
        widgets = {
            'Originalidad': forms.RadioSelect,
            'Importancia': forms.RadioSelect,
            'Coherencia': forms.RadioSelect,
            'Metodologia': forms.RadioSelect,
            'Validez': forms.RadioSelect,
            'Dominio_tema': forms.RadioSelect,
            'sugerencias': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        labels = {
            'Originalidad': 'Originalidad',
            'Importancia': 'Importancia',
            'Coherencia': 'Coherencia',
            'Metodologia': 'Metodología',
            'Validez': 'Validez',
            'Dominio_tema': 'Dominio del tema',
            'sugerencias': 'Sugerencias',
            
        }
 """

class DetalleEvaluacionForm(forms.ModelForm):
    class Meta:
        model = DetalleEvaluacion
        fields = ['originalidad', 'importancia', 'coherencia', 'metodologia', 'validez', 'dominio_tema', 'sugerencias']
        widgets = {
            'originalidad': forms.RadioSelect,
            'importancia': forms.RadioSelect,
            'coherencia': forms.RadioSelect,
            'metodologia': forms.RadioSelect,
            'validez': forms.RadioSelect,
            'dominio_tema': forms.RadioSelect,
            'sugerencias': forms.Textarea(attrs={'rows': 4, 'cols': 40}),

        }
        labels = {
            'originalidad': 'Originalidad',
            'importancia': 'Importancia',
            'coherencia': 'Coherencia',
            'metodologia': 'Metodología',
            'validez': 'Validez',
            'dominio_tema': 'Dominio del tema',
            'sugerencias': 'Sugerencias',
        }