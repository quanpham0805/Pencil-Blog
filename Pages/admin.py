from django.contrib import admin
from .models import PencilType, PencilManufacturer, Pencil, Comment

# Register your models here.

# class PencilTypeAdmin(admin.ModelAdmin):
# 	fieldsets = [
#         ("Type", {'fields': ["type_name"]}),
#         ("Description", {'fields': ["type_description"]}),
#         ("Slug", {'fields': ["type_slug"]}),
#         ("Image", {"fields": ["type_img"]})
#     ]
#     # list_display = ['type_name', 'id', 'type_slug']

# class PencilManugacturerAdmin(admin.ModelAdmin):
#     #ordering = ['manufacturer_name']
#     #list_display = ['manufacturer_name', 'id']
# 	fieldsets = [("Manufacturer", {'fields': ["manufacturer_name"]})]

# class PencilAdmin(admin.ModelAdmin):
# 	fieldsets = [
#         ("Pencil", {'fields': ["pencil_name"]}),
#         ("Description", {'fields': ["pencil_description"]}),
#         ("Author", {'fields': ["pencil_author"]}),
#         ("Published date", {'fields': ["pencil_published_date"]}),
#         ("Slug", {'fields': ["pencil_slug"]}),
#         ("Manufacturer", {'fields': ["pencil_for_manufacturer"]}),
#         ("Image", {"fields": ["pencil_img"]})
#     ]
#     # list_display = ['pencil_name', 'pencil_author', 'pencil_slug', 'pencil_for_manufacturer']

# class CommentAdmin(admin.ModelAdmin):
# 	fieldsets = [
#         ("Post", {'fields': ["comment_post"]}),
#         ("Author", {'fields': ["comment_author"]}),
#         ("Content", {'fields': ["comment_text"]}),
#         ("Published date", {"fields": ["comment_published_date"]})
#     ]
#     # list_display = ['comment_post', 'comment_author', 'comment_published_date']


# admin.site.register(PencilType, PencilTypeAdmin)
# admin.site.register(PencilManufacturer, PencilManugacturerAdmin)
# admin.site.register(Pencil, PencilAdmin)
# admin.site.register(Comment, CommentAdmin)


class PencilManugacturerAdmin(admin.ModelAdmin):
    ordering = ['manufacturer_name']
    list_display = ['manufacturer_name', 'id']

	# fieldsets = [
	# 	("Manufacturer", {
	# 		'fields': ["manufacturer_name"]
	# 	}),
	# ]

admin.site.register(PencilManufacturer, PencilManugacturerAdmin)
