"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('ver/parroquia_barrio', views.listar_Parroquias_Barrios, name='listar_Parroquias_Barrios'),
        path('ver/barrio', views.listar_Barrios, name='listar_Barrios'),
        path('crear/parroquia', views.crear_Parroquia, name='crear_Parroquia'),
        path('crear/barrio_parroquia/<int:id>', views.crear_Barrio_Parroquia, name='crear_Barrio_Parroquia'),
        path('editar/parroquia/<int:id>', views.editar_Parroquia, name='editar_Parroquia'),
        path('editar/barrio/<int:id>', views.editar_Barrio, name='editar_Barrio'),
        path('crear/barrio', views.crear_Barrio, name='crear_Barrio'),
]
