# -*- coding: utf-8 -*-
from django.db import models
import random
import os

# Create your models here.
def get_filename_ext(filepath):
    nombre_base = os.path.basename(filepath)
    nombre, ext = os.path.splitext(nombre_base)
    return nombre, ext

def upload_image_pathb(instancia, nombrearchivo):
    # print(instancia)
    # print(nombrearchivo)
    nuevo_nombrearchivo = random.randint(1,3910209312)
    nombre, ext = get_filename_ext(nombrearchivo)
    nombrearchivo_final = '{nuevo_nombrearchivo}{ext}'.format(nuevo_nombrearchivo=nuevo_nombrearchivo,ext=ext)
    return "almacen/c-b/{nuevo_nombrearchivo}/{nombrearchivo_final}".format(
            nuevo_nombrearchivo=nuevo_nombrearchivo,
            nombrearchivo_final=nombrearchivo_final
            )

def upload_image_path(instancia, nombrearchivo):
    # print(instancia)
    # print(nombrearchivo)
    nuevo_nombrearchivo = random.randint(1,3910209312)
    nombre, ext = get_filename_ext(nombrearchivo)
    nombrearchivo_final = '{nuevo_nombrearchivo}{ext}'.format(nuevo_nombrearchivo=nuevo_nombrearchivo,ext=ext)
    return "almacen/miniaturas/{nuevo_nombrearchivo}/{nombrearchivo_final}".format(
            nuevo_nombrearchivo=nuevo_nombrearchivo,
            nombrearchivo_final=nombrearchivo_final
            )

class Almacen(models.Model):
    codigo = models.CharField(max_length=50,blank=True,null=True)
    cod_barras = models.ImageField(upload_to=upload_image_pathb, null=True, blank=True)
    descripcion = models.CharField(max_length=200,blank=True,null=True)
    medida = models.CharField(max_length=50,blank=True,null=True)
    unidad = models.CharField(max_length=50,blank=True,null=True)
    existencia = models.PositiveIntegerField(blank=True, null=True)
    cantidad_caja = models.PositiveIntegerField(blank=True, null=True)
    cantidad_rb = models.PositiveIntegerField(blank=True, null=True)
    proveedor = models.CharField(max_length=50,blank=True,null=True)
    ubicacion = models.CharField(max_length=50,blank=True,null=True)
    costo = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=6)
    def __str__(self):
        return self.codigo
