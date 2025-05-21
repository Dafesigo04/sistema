from django.db import models

# Create your models here.

class Citas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, verbose_name='Nombres')
    apellido = models.CharField(max_length=150, verbose_name='Apellidos')
    correo = models.EmailField(max_length=40, verbose_name='Correo')
    documento = models.IntegerField(verbose_name='N° de documento')
    fecha = models.DateField(verbose_name='Fecha')
    hora = models.CharField(max_length=10, verbose_name='Horas')
    servicio = models.CharField(max_length=100, verbose_name="Servicio", null=True)

    def __str__(self):
        fila ="Nombres: " + self.nombre + " - " + "Apellidos: " + self.apellido + " - " + "Correo: " + self.correo  + " - " + "Servicio: " + self.servicio
        return fila

