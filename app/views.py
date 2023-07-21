from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    if(request.method == "POST"):
        return redirect('menu')
    return render(request,'login.html',{})

def periodo(request):
    return render(request,'periodo.html',{})

def menu(request):
    return render(request,'Menu.html',{})

def unidad(request):
    return render(request,'unidad.html',{})


def usuario(request):
    return render(request,'usuario.html',{})

def rol(request):
    return render(request,'rol.html',{})

def contenido(request):
    return render(request,'contenido.html',{})

def malla(request):
    if(request.method == "POST"):
        return redirect('doc')
    return render(request,'malla.html',{})


def documento(request):
    return render(request,'documento.html',{})