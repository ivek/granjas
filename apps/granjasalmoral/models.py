from django.db import models

# Create your models here.
class InfoPersonal(models.Model):#informacion del personal
    id_personal=models.CharField(max_length=30)#identificador del personal
    pwd_personal=models.CharField(max_length=50)#contraseña
    nombre=models.CharField(max_length=50)#nombre del empleado
    apellidos=models.CharField(max_length=200)#apellidos dl empleado
    curp=models.CharField(max_length=50)
    rfc=models.CharField(max_length=30)
    edad=models.IntegerField(default=0)
    genero=models.CharField(max_length=20)
    edo_civil=models.CharField(max_length=20)
    direccion=models.TextField()
    telefono=models.CharField(max_length=20)
    email=models.EmailField()
    facebook=models.CharField(max_length=100)
    otra_red=models.CharField(max_length=100)
    puesto=models.CharField(max_length=200)#pùesto que desempeña en la empresa
    hra_entrada=models.TimeField()#hora de entrada
    hra_salida=models.TimeField()#hora de salida
    fech_engreso_empresa=models.DateField()#fecha de ingreso a la empresa
    fech_engreso_cooperativa=models.DateField()#fecha de ingreso a la cooperativa
    img = models.FileField(upload_to='uploads/',default="")#imagen de identificacion

class Jornada(models.Model):#jornada laboral
    id_personal=models.CharField(max_length=30)#identificador del personal
    fech_actual=models.DateField()#dia actual que labora
    hra_in=models.TimeField()#hora en que entro a laboral el dia
    hra_out=models.TimeField()#hora en que salio a laboral el dia
    retardo=models.BooleanField()#llegada despues de la hora de entrada laboral
    justificado=models.BooleanField()#justificar el dia laboral
    comision_personal=models.BooleanField()#si esta comisionado en alguna otro lugar. 
    lugar_trabajo=models.CharField(max_length=200)#coordenadas de geolocaizacion
    observacion=models.TextField()#informacion adicional

class comision(models.Model):#salir del centro de trabajo
    id_personal=models.CharField(max_length=30)#identificador del personal
    lugar_salida=models.CharField(max_length=100)#clugar donde sale
    lugar_destinomodels.CharField(max_length=100)#clugar donde llega
    distancia=models.CharField(max_length=50)#distancia de origen - destno
    vehiculo=models.CharField(max_length=50)#placas de identificacion del vehiculo
    fecha_orden=models.DateField()#fecha cuando fue comisionado

class justificante(models.Model):#datos para justificar inasitencia
     id_personal=models.CharField(max_length=30)#identificador del personal
     motivo=models.TextField()#expone motivos que amparen lajustificacion de inasitencia
     fecha_justificante=models.DateField()#fecha que se esta justificando
     tiempo=models.TimeField()#numerode horas que se justificante
     soporte=models.FileField(upload_to='uploads/',default="")#archivo que ampara la inasistencia

class prestamo(models.Model):#control prestamos que se otorga al empleado
      id_personal=models.CharField(max_length=30)#identificador del personal
      concepto=models.CharField(max_length=50)#detalle del prestamo
      cantidad_ini=models.DecimalField()#cantidad total que se presto
      cantidad_rest=models.DecimalField()#cantidad restante del prestamo
      plazo=models.IntegerField()#numero de pagos que se van a descntar
      cobro=models.DecimalField()#cantidad del descuento que se realizara en nomina
      fecha_prest=models.DateField()#fecha del prestamo
