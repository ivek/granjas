from django.db import models

# Create your models here.
class InfoPersonal(models.Model):
    id_personal=models.CharField(max_length=30)
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=200)
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
    puesto=models.CharField(max_length=200)
    hra_entrada=models.DateTimeField()
    hra_salida=models.DateTimeField()
    fech_engreso=models.DateField()
    img = models.FileField(upload_to='uploads/',default="")
