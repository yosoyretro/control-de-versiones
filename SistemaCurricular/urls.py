"""
URL configuration for SistemaCurricular project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app import views
urlpatterns = [
    path('',views.login,name='login'),
    path('menu/',views.menu,name='menu'),
    path('crear-usuario',views.usuario,name='usuario'),
    path('crear-rol',views.rol,name='rol'),
    path('crear-contenidos',views.contenido,name='contenido'),
    path('crear-unidad',views.unidad,name='unidad'),
    path('crear-periodo',views.periodo,name='periodo'),
    path('crear-malla',views.malla,name='malla'),
    path('crear-periodo',views.periodo,name="periodo"),
    path('documento',views.documento,name="doc")
]
