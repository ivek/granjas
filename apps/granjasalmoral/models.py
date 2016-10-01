from django.db import models
from decimal import Decimal

# Create your models here.
    
class empresas(models.Model):
    razon_social=models.CharField(max_length=50)#nombre de la empresa
    rfc=models.CharField(max_length=50)#rfc
    apoderado=models.CharField(max_length=50)#nombre del apoderado
    direccion=models.TextField(max_length=50)#direccion 


class InfoPersonal(models.Model):#informacion del personal
    id_personal=models.CharField(max_length=30, null=True, blank=True)#identificador del personal
    pwd_personal=models.CharField(max_length=50, default="")#contraseña
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
    sueldo=models.DecimalField(max_digits=15,decimal_places=2,default=Decimal('0.00'))
    #hra_entrada=models.TimeField(null=True, blank=True)#hora de entrada
    #hra_salida=models.TimeField(null=True, blank=True)#hora de salida
    #fech_ingreso_empresa=models.DateField(null=True, blank=True)#fecha de ingreso a la empresa
    #fech_ingreso_cooperativa=models.DateField(null=True, blank=True)#fecha de ingreso a la cooperativa
    razon_social=models.ForeignKey(empresas, null=True, blank=True)#identificador del personal
    img = models.FileField(upload_to='uploads/', null=True)#imagen de identificacion

class Jornada(models.Model):#jornada laboral
    id_personal=models.ForeignKey(InfoPersonal, null=True, blank=True, on_delete=models.CASCADE)#identificador del personal
    #fech_actual=models.DateField(null=True, blank=True)#dia actual que labora
    #hra_in=models.TimeField(null=True, blank=True)#hora en que entro a laboral el dia
    #hra_out=models.TimeField(null=True, blank=True)#hora en que salio a laboral el dia
    retardo=models.BooleanField()#llegada despues de la hora de entrada laboral
    justificado=models.BooleanField()#justificar el dia laboral
    comision_personal=models.BooleanField()#si esta comisionado en alguna otro lugar. 
    lugar_trabajo=models.CharField(max_length=200)#coordenadas de geolocaizacion
    observacion=models.TextField()#informacion adicional

class comision(models.Model):#salir del centro de trabajo
    id_personal=models.ForeignKey(InfoPersonal, null=True, blank=True, on_delete=models.CASCADE)#identificador del personal
    lugar_salida=models.CharField(max_length=100)#clugar donde sale
    lugar_destino=models.CharField(max_length=100)#clugar donde llega
    distancia=models.CharField(max_length=50)#distancia de origen - destno
    vehiculo=models.CharField(max_length=50)#placas de identificacion del vehiculo
    #fecha_orden=models.DateField(null=True, blank=True)#fecha cuando fue comisionado

class justificante(models.Model):#datos para justificar inasitencia
     id_personal=models.ForeignKey(InfoPersonal, null=True, blank=True, on_delete=models.CASCADE)#identificador del personal
     motivo=models.TextField()#expone motivos que amparen lajustificacion de inasitencia
     #fecha_justificante=models.DateField(null=True, blank=True)#fecha que se esta justificando
     #tiempo=models.TimeField(null=True, blank=True)#numerode horas que se justificante
     soporte=models.FileField(upload_to='uploads/',null=True)#archivo que ampara la inasistencia

class prestamo(models.Model):#control prestamos que se otorga al empleado
      id_personal=models.ForeignKey(InfoPersonal, null=True, blank=True, on_delete=models.CASCADE)
      concepto=models.CharField(max_length=50)#detalle del prestamo
      cantidad_ini=models.DecimalField(max_digits=15,decimal_places=2,default=Decimal('0.00'))#cantidad total que se presto
      cantidad_rest=models.DecimalField(max_digits=15,decimal_places=2,default=Decimal('0.00'))#cantidad restante del prestamo
      plazo=models.IntegerField()#numero de pagos que se van a descntar
      letras_pagos=models.DecimalField(max_digits=15,decimal_places=2,default=Decimal('0.00'))#cantidad del descuento que se realizara en nomina
      #fecha_prest=models.DateField(null=True, blank=True)#fecha del prestamo
      pagare = models.FileField(upload_to='uploads/',null=True)#imagen de pagare que soporte el prestamo dado
