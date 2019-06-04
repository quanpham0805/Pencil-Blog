from django.db import models
from datetime import datetime

# Create your models here

class PencilType(models.Model):
    type_name = models.CharField(max_length=100)
    type_summary = models.CharField(max_length=300)
    #type_img =
    type_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.type_name

class PencilManufacturer(models.Model):
    manufacturer_for_type = models.ForeignKey(PencilType, default=1, verbose_name="Type", on_delete=models.SET_DEFAULT)
    manufacturer_name = models.CharField(max_length=100)
    manufacturer_description = models.CharField(max_length=300)
    manufacturer_img =

    def __str__(self):
        return self.manufacturer_name

class Pencil(models.Model):
    pencil_name = models.CharField(max_length=200)
    pencil_description = models.TextField()
    pencil_published = models.DateTimeField('date published')
    pencil_author =
    pencil_comment =
    pencil_img =