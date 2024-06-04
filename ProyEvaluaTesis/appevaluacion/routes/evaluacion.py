
from django.urls import path
from appevaluacion.views import evaluacion


urlpatterns = [  
   #path('',evaluacion.evaluar ,name="evaluar"),
   path('',evaluacion.listar_evaluaciones ,name="listar_evaluaciones"),
   path('listar_evaluacion_json', evaluacion.listar_evaluacion_json,name="listar_evaluacion_json"), 

   
]