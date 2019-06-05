from django.contrib import admin
from .models import PencilType, PencilManufacturer, Pencil, Comment

# Register your models here.

admin.site.register(PencilType)
admin.site.register(PencilManufacturer)
admin.site.register(Pencil)
admin.site.register(Comment)
