from django.contrib import admin
from .models import PencilType, PencilManufacturer, Pencil, Comment

# Register your models here.

class PencilTypeAdmin(admin.ModelAdmin):
	odering = ['type_name']
	list_display = ['id', 'type_name', 'type_slug']
	search_fields = ['type_name', 'type_description']
	fieldsets = [
		('Type', {'fields': ['type_name']}),
		("Description", {'fields': ["type_description"]}),
		("Slug", {'fields': ["type_slug"]}),
		("Image", {"fields": ["type_img"]})
	]

class PencilManugacturerAdmin(admin.ModelAdmin):
    ordering = ['manufacturer_name']
    list_display = ['id', 'manufacturer_name', 'manufacturer_for_type']
    search_fields = ['manufacturer_name', 'manufacturer_description']
    fieldsets = [
    	('Manufacturer', {'fields': ['manufacturer_name']}),
		("Description", {'fields': ["manufacturer_description"]}),
		("Type", {'fields': ["manufacturer_for_type"]}),
		("Image", {"fields": ["manufacturer_img"]})
    ]

class PencilAdmin(admin.ModelAdmin):
	ordering = ['pencil_published_date']
	list_display = ['pencil_name', 'pencil_author', 'pencil_slug', 'pencil_for_manufacturer']
	search_fields = ['pencil_name', 'pencil_description', 'pencil_for_manufacturer']
	list_filter = ['pencil_author', 'pencil_published_date']
	fieldsets = [
		("Pencil", {'fields': ["pencil_name"]}),
        ("Description", {'fields': ["pencil_description"]}),
        ("Author", {'fields': ["pencil_author"]}),
        ("Published date", {'fields': ["pencil_published_date"]}),
        ("Slug", {'fields': ["pencil_slug"]}),
        ("Manufacturer", {'fields': ["pencil_for_manufacturer"]}),
        ("Image", {"fields": ["pencil_img"]})
	]

class CommentAdmin(admin.ModelAdmin):
	ordering = ['comment_published_date']
	list_display = ['comment_post', 'comment_author', 'published_date']
	search_fields = ['comment_text']
	list_filter = ['comment_author', 'comment_published_date']
	fieldsets = [
		("Post", {'fields': ["comment_post"]}),
        ("Author", {'fields': ["comment_author"]}),
        ("Content", {'fields': ["comment_text"]}),
        ("Published date", {"fields": ["comment_published_date"]})
	]

admin.site.register(PencilType, PencilTypeAdmin)
admin.site.register(PencilManufacturer, PencilManugacturerAdmin)
admin.site.register(Pencil, PencilAdmin)
admin.site.register(Comment, CommentAdmin)