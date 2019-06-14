# customize the admin.

from django.contrib import admin
from .models import PencilType, PencilManufacturer, Pencil, Comment

# Register your models here.

# admin for the type.
class PencilTypeAdmin(admin.ModelAdmin):
	# oder by the name, display id, type_name and type_slug column, allow
	# search name and description, and the fields to display clean data settings.
	odering = ['type_name']
	list_display = ['id', 'type_name', 'type_slug']
	search_fields = ['type_name', 'type_description']
	fieldsets = [
		('Type', {'fields': ['type_name']}),
		("Description", {'fields': ["type_description"]}),
		("Slug", {'fields': ["type_slug"]}),
		("Image", {"fields": ["type_img"]})
	]

# manufacturer admin
class PencilManugacturerAdmin(admin.ModelAdmin):
	# oder by name, display id, name and type corresponding
	# allow search name and description
	# use fieldset to group the setting in the manufacturer
    ordering = ['manufacturer_name']
    list_display = ['id', 'manufacturer_name', 'manufacturer_for_type']
    search_fields = ['manufacturer_name', 'manufacturer_description']
    fieldsets = [
    	('Manufacturer', {'fields': ['manufacturer_name']}),
		("Description", {'fields': ["manufacturer_description"]}),
		("Type", {'fields': ["manufacturer_for_type"]}),
		("Image", {"fields": ["manufacturer_img"]})
    ]

# admin for pencil.
class PencilAdmin(admin.ModelAdmin):
	# oder by date published newest to oldest
	# display name, author, slug and the corresponding manufacturer
	# allow search for name, description
	# allow filter author and published date
	# field set to group setting
	ordering = ['-pencil_published_date']
	list_display = ['pencil_name', 'pencil_author', 'pencil_slug', 'pencil_for_manufacturer']
	search_fields = ['pencil_name', 'pencil_description']
	list_filter = ['pencil_author', 'pencil_published_date']
	fieldsets = [
		("Pencil", {'fields': ["pencil_name"]}),
        ("Description", {'fields': ["pencil_description", "pencil_brief_description"]}),
        ("Author", {'fields': ["pencil_author"]}),
        ("Published date", {'fields': ["pencil_published_date"]}),
        ("Slug", {'fields': ["pencil_slug"]}),
        ("Manufacturer", {'fields': ["pencil_for_manufacturer"]}),
        ("Image", {"fields": ["pencil_img"]})
	]

# admin for comment.
class CommentAdmin(admin.ModelAdmin):
	# oder newest to oldest comment
	# display the post that comment, corresponding post, author and published date
	# filter by author and date
	# allow search for text
	# field set to group the settings
	ordering = ['-comment_published_date']
	list_display = ['comment_text', 'comment_post', 'comment_author', 'published_date']
	search_fields = ['comment_text']
	list_filter = ['comment_author', 'comment_published_date']
	fieldsets = [
		("Post", {'fields': ["comment_post"]}),
        ("Author", {'fields': ["comment_author"]}),
        ("Content", {'fields': ["comment_text"]}),
        ("Published date", {"fields": ["comment_published_date"]})
	]

# then register to the homepage.
admin.site.register(PencilType, PencilTypeAdmin)
admin.site.register(PencilManufacturer, PencilManugacturerAdmin)
admin.site.register(Pencil, PencilAdmin)
admin.site.register(Comment, CommentAdmin)