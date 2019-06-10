from django.contrib import admin
from .models import PencilType, PencilManufacturer, Pencil, Comment

# Register your models here.

# class PencilTypeAdmin(admin.ModelAdmin):


# class PencilManugacturerAdmin(admin.ModelAdmin):


# class PencilAdmin(admin.ModelAdmin):


# class CommentAdmin(admin.ModelAdmin):



# admin.site.register(PencilType, PencilTypeAdmin)
# admin.site.register(PencilManufacturer, PencilManugacturerAdmin)
# admin.site.register(Pencil, PencilAdmin)
# admin.site.register(Comment, CommentAdmin)

admin.site.register(PencilType)
admin.site.register(PencilManufacturer)
admin.site.register(Pencil)
admin.site.register(Comment)
