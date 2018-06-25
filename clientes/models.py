from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Cliente(models.Model):
	nombre = models.CharField(max_length=50,blank=False)
	apellidos = models.CharField(max_length=50,blank=False)
	direccion = models.CharField(max_length=255,blank=True)
	email = models.EmailField(max_length=50,blank=False)
	telefono = models.CharField(max_length=20,blank=False)
	celular = models.CharField(max_length=25,blank=True)
	empresa = models.CharField(max_length=50,blank=False)
	ejecutivo = models.CharField(max_length=50,blank=True)
	usuario = models.IntegerField(blank=False)
	fecha_registro = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.nombre
