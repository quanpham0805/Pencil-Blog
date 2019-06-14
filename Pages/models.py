from django.db import models
from django.utils import timezone
import pytz
from django.conf import settings
timezone.activate(settings.TIME_ZONE)

# Create your models here

class PencilType(models.Model):
    type_name = models.CharField(max_length=100)
    type_description = models.CharField(max_length=300)
    type_slug = models.CharField(max_length=200, default=1)
    type_img = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.type_name

    class Meta:
        unique_together = ['type_slug']

class PencilManufacturer(models.Model):
    manufacturer_for_type = models.ForeignKey(PencilType, default=1, verbose_name="Type", on_delete=models.SET_DEFAULT)
    manufacturer_name = models.CharField(max_length=100)
    manufacturer_description = models.CharField(max_length=300)
    manufacturer_img = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        unique_together = ['manufacturer_name']

class Pencil(models.Model):
    pencil_for_manufacturer = models.ForeignKey(PencilManufacturer, default=1, verbose_name="Pencil", on_delete=models.SET_DEFAULT)
    pencil_name = models.CharField(max_length=200)
    pencil_brief_description = models.CharField(max_length=300, default="pencils")
    pencil_description = models.TextField()
    pencil_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pencil_published_date = models.DateTimeField(timezone.localtime(timezone.now()))
    pencil_slug = models.CharField(max_length=200, default=1)
    pencil_img = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.pencil_name

    class Meta:
        unique_together = ['pencil_slug', 'pencil_name']

class Comment(models.Model):
    comment_post = models.ForeignKey(Pencil, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_published_date = models.DateTimeField(default=timezone.localtime(timezone.now()))

    def published_date(self):
        return self.comment_published_date

    def __str__(self):
        return self.comment_text[:25]