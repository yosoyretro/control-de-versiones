from django.db import models

# Create your models here.º



class Periodo(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.nombre


class ProductoAcademico(models.Model):
    objetivo = models.TextField()
    producto_parcial = models.TextField()
    resultado_estandares = models.TextField()
    integracion_carreras = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Producto Academico {self.id}"


class AmbienteAprendizaje(models.Model):
    metodo_ensenanza = models.TextField()
    medios = models.TextField()
    evaluacion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Ambiente de Aprendizaje {self.id}"


class Asignatura(models.Model):
    nombre = models.CharField(max_length=500)
    aporte_tmap = models.TextField()
    requisitos = models.TextField()
    objetivo = models.TextField()
    objetivos_especificos = models.TextField()
    descripcion_producto_academico = models.TextField()
    id_producto_academico = models.ForeignKey(ProductoAcademico, on_delete=models.CASCADE)
    id_periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    id_ambiente_aprendisaje = models.ForeignKey(AmbienteAprendizaje, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre


class Referencia(models.Model):
    tipo = models.CharField(max_length=100,unique=True)
    numero = models.IntegerField()
    descripcion = models.TextField()
    descri_existencia = models.TextField()
    descri_numero_ejemplares = models.TextField()
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Referencia {self.id}"


class Unidad(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=500)
    objetivo = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Unidad {self.id}"


class Contenido(models.Model):
    numero = models.IntegerField()
    nombre = models.TextField()
    horas_docencias = models.IntegerField()
    horas_gestion_practica = models.IntegerField()
    minutos_practicas_docencias = models.IntegerField()
    horas_autonomas = models.IntegerField()
    id_unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Contenido {self.id}"


class Subcontenido(models.Model):
    numero = models.IntegerField()
    id_contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Subcontenido {self.id}"


class Rol(models.Model):
    nombre = models.CharField(max_length=500,unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Trabajador(models.Model):
    cedula = models.CharField(max_length=15,unique=True)
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    usuario = models.CharField(max_length=150, unique=True)
    clave = models.CharField(max_length=150)
    ruta = models.TextField()
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trabajador {self.id}"


class DatosInformativos(models.Model):
    prerequisitos = models.TextField()
    total_horas_docencia = models.IntegerField()
    total_horas_practicas = models.IntegerField()
    total_horas_docente = models.IntegerField()
    total_horas_autonomas = models.IntegerField()
    horas_trabajos_autonomo = models.IntegerField()
    id_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    id_unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    jefe_area = models.ForeignKey(Trabajador, related_name='jefe_area', on_delete=models.CASCADE)
    coordinador_carrera = models.ForeignKey(Trabajador, related_name='coordinador_carrera', on_delete=models.CASCADE)
    responsable1 = models.ForeignKey(Trabajador, related_name='responsable1', on_delete=models.CASCADE)
    responsable2 = models.ForeignKey(Trabajador, related_name='responsable2', on_delete=models.CASCADE)
    responsable3 = models.ForeignKey(Trabajador, related_name='responsable3', on_delete=models.CASCADE)
    fecha_entrega = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Datos Informativos {self.id}"