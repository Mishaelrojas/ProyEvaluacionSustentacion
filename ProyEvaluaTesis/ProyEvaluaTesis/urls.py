"""
URL configuration for ProyEvaluaTesis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appevaluacion.views import evaluacion,views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Accesos
    path('', views.acceder, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.salir ,name="logout"),


    path('evaluacion/',include('appevaluacion.routes.evaluacion')),
    path('ponente/',include('appevaluacion.routes.ponente')),
    path('detalle/',include('appevaluacion.routes.detalle_evaluacion')),


    path('create-detalle/',evaluacion.crear_detalle_evaluacion ,name="crear_detalle_evaluacion"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)