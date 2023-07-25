from django.shortcuts import render,redirect,get_object_or_404
from app.models import Rol,Trabajador,Periodo,Unidad,ProductoAcademico,AmbienteAprendizaje,Asignatura,DatosInformativos,Contenido,Asignaciones

def login(request):           
    return render(request,'login.html',{})

def periodo(request):
    mensaje = ""
    if(request.method == "POST"):
        nombreP = request.POST["nombre"]
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
    mensaje = ""
    if(request.method == "POST"):
        n = request.POST["numero"]
        ob = request.POST["objetivo"]
        obu = Unidad(numero=n,nombre=ob)
        obu.save()
        mensaje = "Unidad guardada con exito !"
    return render(request,'unidad.html',{'msg':mensaje})

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
    mensaje = ""

    if request.method == "POST":
        try:
            #PRODUCTO ACADEMICO 
            objetivoPA = request.POST["obj-productoAcademico"]
            productoPa = request.POST["obj-productoParcial"]
            resultadosE = request.POST["obj-resultadoEstandaresPresentacion"]
            integracionC = request.POST["obj-integracionAsignaturas"]
            #AMBIENTE DE APRENDISAJE
            variabelMetodosE = request.POST["amb-metodoEnseñanza"]
            variableMedios = request.POST["amb-medios"]
            variableEvaluacion = request.POST["amb-evaluacion"]
            #ASIGNATURA
            nombreAsignatura = request.POST["nombre-asignatura"]
            aportes = request.POST["aporte-teoricos"]
            requisitos = request.POST["requisitos"]
            objetivosA = request.POST["objetivos-asignaturas"]
            objetivosE = request.POST["objetivos-especificos"]
            descripProducuto = request.POST["descripcion-producto-academico"]
            periodo = request.POST["opciones"]
            periodoobj = get_object_or_404(Periodo,id=periodo)
            #AGREGAR LOS VALORES DE PRODUCTO ACADEMICO
            objProductoA = ProductoAcademico(objetivo=objetivoPA,producto_parcial=productoPa,resultado_estandares=resultadosE,integracion_carreras=integracionC)
            objProductoA.save()
            #AGREGAR LOS VALORES DE AMBIENTE DE APREDNISAJE 
            objAA = AmbienteAprendizaje(metodo_ensenanza=variabelMetodosE,medios=variableMedios,evaluacion=variableEvaluacion)
            objAA.save()
            #AGREGAR LS VALORES DE ASIGNATURAS 
            varRol = Asignatura(nombre=nombreAsignatura,
                                aporte_tmap=aportes,
                                requisitos=requisitos,
                                objetivo=objetivosA,
                                objetivos_especificos=objetivosE,
                                descripcion_producto_academico=descripProducuto,
                                id_producto_academico=objProductoA,
                                id_periodo=periodoobj,
                                id_ambiente_aprendisaje=objAA)
            varRol.save()
            mensaje = True
        except:
            mensaje = False
    
    dataperiodo = Periodo.objects.all()   
    return render(request,'asignatura.html',{
        'dataperiodo':dataperiodo,
        'msg':mensaje
    })

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
    obja = Asignatura.objects.all()
    obju = Unidad.objects.all()

    if (request.method == "POST"):
        lista = []
        
        for i in request.POST:
            lista.append(request.POST.get(i))

        obj1 = Contenido(numero=lista[3],nombre=lista[4],horas_docencias=lista[5],horas_gestion_practica=lista[6],minutos_practicas_docencias=lista[7],horas_autonomas=lista[8])
        obj1.save()
        
        obj2 = Contenido(numero=lista[9],nombre=lista[10],horas_docencias=lista[11],horas_gestion_practica=lista[12],minutos_practicas_docencias=lista[13],horas_autonomas=lista[14])
        obj2.save()
        
        obj3 = Contenido(numero=lista[15],nombre=lista[16],horas_docencias=lista[17],horas_gestion_practica=lista[18],minutos_practicas_docencias=lista[19],horas_autonomas=lista[20])
        obj3.save()
        
        obj4 = Contenido(numero=lista[21],nombre=lista[22],horas_docencias=lista[23],horas_gestion_practica=lista[24],minutos_practicas_docencias=lista[25],horas_autonomas=lista[26])
        obj4.save()

        Asignaciones(id_contenido=obj1,id_unidad=get_object_or_404(Unidad,id=lista[2]),id_asignaturas=get_object_or_404(Asignatura,id=lista[1])).save()
        Asignaciones(id_contenido=obj2,id_unidad=get_object_or_404(Unidad,id=lista[2]),id_asignaturas=get_object_or_404(Asignatura,id=lista[1])).save()
        Asignaciones(id_contenido=obj3,id_unidad=get_object_or_404(Unidad,id=lista[2]),id_asignaturas=get_object_or_404(Asignatura,id=lista[1])).save()
        Asignaciones(id_contenido=obj4,id_unidad=get_object_or_404(Unidad,id=lista[2]),id_asignaturas=get_object_or_404(Asignatura,id=lista[1])).save()
        

    return render(request,'contenido.html',{
        'asignatura':obja,
        'unidad':obju
    })

def malla(request):
    objtra = Trabajador.objects.all()
    objasig = Asignatura.objects.all()
    
    if(request.method == "POST"):
        lista = []
        
        for i in request.POST:
            lista.append(request.POST.get(i)) 
        
        #FIRMAS DE RESPONSABILIDAD
        referencia1 = get_object_or_404(Trabajador,id = lista[11])
        referencia2 = get_object_or_404(Trabajador,id = lista[12])
        referencia3 = get_object_or_404(Trabajador,id = lista[13])
        cordinado = get_object_or_404(Trabajador,id = lista[14])
        jefe = get_object_or_404(Trabajador,id = lista[15])
        id_asignatura = get_object_or_404(Trabajador,id = lista[15])

        #obja = Asignatura(nombre=)    
        
        #REFERENCIAS
        bn = lista[1]
        bt = lista[2]
        beb = lista[3]
        bne = lista[4]
        
        cn = lista[5]
        ct = lista[6]
        ceb = lista[7]
        cne = lista[8]
        
        wn = lista[9]
        wd = lista[10]
        
        return redirect('doc')
    
    return render(request,'malla.html',{'trabajadores':objtra,'asignaturas':objasig})

def documento(request):
    return render(request,'documento.html',{})