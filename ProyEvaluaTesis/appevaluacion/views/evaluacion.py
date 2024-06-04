from django.shortcuts import render, redirect,  get_object_or_404
from appevaluacion.models import Alumno, Evaluacion, Jurado, DetalleEvaluacion
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#@login_required(login_url='login')
def listar_evaluaciones(request): 
    jurados_presidente = Jurado.objects.filter(cargo='Presidente')
    jurados_secretario = Jurado.objects.filter(cargo='Secretario') 
    return render(request, "evaluacion/listar.html", {'jurados_presidente':jurados_presidente,'jurados_secretario':jurados_secretario})


#@login_required(login_url='login')
def listar_evaluacion_json(_request):    
    evaluacion = list(Evaluacion.objects.values())
    alumnos = {alumno['idAlumno']: alumno for alumno in Alumno.objects.values()}

    data = {'evaluacion':evaluacion, 'alumnos':alumnos}
    return JsonResponse(data)



@csrf_exempt
def crear_detalle_evaluacion(request):

    if request.method == 'POST':         
        idEvaluacion = request.POST.get('id_evaluacion')
        print(idEvaluacion)
        juradoid = request.POST.get('id_jurado_presidente')
        print(juradoid)
        try:
            #id_evaluacion = int(idEvaluacion)
           # id_jurado_presidente = int(jurado_id)

            #jurado = Jurado.objects.get(idJurado=id_jurado_presidente)
            detalle_evaluacion = DetalleEvaluacion.objects.create(
               eliminado=False,
               jurado_id=juradoid,
               evaluacion_id=idEvaluacion,
               #evaluacion_id=id_evaluacion
            )
            return JsonResponse({'mensaje': f'Jurado con ID {1} asignado con éxito a la evaluación {1}'})
        except Jurado.DoesNotExist:
            return JsonResponse({'error': 'Jurado no encontrado'}, status=404)
        except ValueError:
            return JsonResponse({'error': 'ID no válido'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return render(request, 'evaluador/listar.html')





def evaluar(request):
    return render(request, "evaluacion/evaluacion.html")

