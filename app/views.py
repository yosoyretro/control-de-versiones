from django.shortcuts import render,redirect,get_object_or_404
from app.models import Rol,Trabajador,Periodo
# Create your views here.

def login(request):
            
    return render(request,'login.html',{})

def periodo(request):
    mensaje = ""

    if(request.method == "POST"):
        print("Me cumplo el motodo post  ")
        nombreP = request.POST["nombre"]
        print(nombreP)
        try:
            objp = Periodo(nombre=nombreP)
            objp.save()
        except:
            mensaje = False

        mensaje = True
    return render(request,'periodo.html',{'msg':mensaje})

def menu(request):
    return render(request,'Menu.html',{})

def unidad(request):
    return render(request,'unidad.html',{})


def usuario(request):
    mensaje = ""
    
    if (request.method == "POST"):
        try:
            cedula = request.POST["cedula"]
            nombres = request.POST["nombres"]   
            apellidos = request.POST["apellidos"] 
            usuario = request.POST["cedula"]
            clave = request.POST["cedula"]
            numero_rol = request.POST.get("opciones")    
            rolo = get_object_or_404(Rol, id=numero_rol)
            objt = Trabajador(cedula=cedula,nombres=nombres,apellidos=apellidos,usuario=usuario,clave=clave,ruta="/img",id_rol=rolo)
            objt.save()
            mensaje = True
        except:
            mensaje = False

    rol = Rol.objects.all()

    return render(request,'usuario.html',{'rol':rol,'msg':mensaje})

def asignatura(request):
    return render(request,'asignatura.html',{})

def rol(request):
    mensaje = ""
    if (request.method == "POST"):
        nombre = request.POST["nombre-rol"]   
        try:    
            objr = Rol(nombre=nombre)
            objr.save() 
            mensaje = True
        except:
            mensaje = False

    return render(request,'rol.html',{'msg':mensaje})

def contenido(request):
    return render(request,'contenido.html',{})

def malla(request):
    if(request.method == "POST"):
        return redirect('doc')
    return render(request,'malla.html',{})


def documento(request):
    return render(request,'documento.html',{})