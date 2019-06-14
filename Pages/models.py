# import needed stuffs
# the model, how our databse is define.

from django.db import models
from django.utils import timezone
import pytz
from django.conf import settings
# activate time in the current timezone
timezone.activate(settings.TIME_ZONE)


# type of pencil. This will be used in the home page
class PencilType(models.Model):
    # we have the type name, description, slug for url, and the image
    type_name = models.CharField(max_length=100)
    type_description = models.CharField(max_length=300)
    type_slug = models.CharField(max_length=200, default=1)
    type_img = models.ImageField(upload_to='images', blank=True)

    # we use the name in admin to see clearly
    def __str__(self):
        return self.type_name

    # meta class with unique together means the slug is unique.
    class Meta:
        unique_together = ['type_slug']

# the manufacturer of the pencils.
class PencilManufacturer(models.Model):
    # the foreign key is this table relative to the type table. It will have
    # relationship like parent and child on the tree.
    # then we have the name, description and image.
    # on_delete set default is when we delete the type, this table will not be deleted, but rather
    # set the default value, which is 1.
    manufacturer_for_type = models.ForeignKey(PencilType, default=1, verbose_name="Type", on_delete=models.SET_DEFAULT)
    manufacturer_name = models.CharField(max_length=100)
    manufacturer_description = models.CharField(max_length=300)
    manufacturer_img = models.ImageField(upload_to='images', blank=True)

    # the name in the admin page will be the manufacturer name
    def __str__(self):
        return self.manufacturer_name

    # the name must be unique so it will not be confused
    class Meta:
        unique_together = ['manufacturer_name']

# the pencil model used in the main page
class Pencil(models.Model):
    # this pencil has foreign key to the manufacturer.
    pencil_for_manufacturer = models.ForeignKey(PencilManufacturer, default=1, verbose_name="Pencil", on_delete=models.SET_DEFAULT)
    # the information about this pencil.
    # author will be the foreign key to the author's database. on_delete=models.CASCADE means if the user is deleted, this table will be deleted.
    pencil_name = models.CharField(max_length=200)
    pencil_brief_description = models.CharField(max_length=300, default="pencils")
    pencil_description = models.TextField()
    pencil_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pencil_published_date = models.DateTimeField(timezone.localtime(timezone.now()))
    pencil_slug = models.CharField(max_length=200, default=1)
    pencil_img = models.ImageField(upload_to='images', blank=True)

    # in admin, the pencil name will be displayed
    def __str__(self):
        return self.pencil_name

    # pencil slug and name must be unique
    class Meta:
        unique_together = ['pencil_slug', 'pencil_name']

# comment model
class Comment(models.Model):
    # use the foreign key to indicate that the comment belongs to the post.
    # author will be the foreign key to the author's database.
    comment_post = models.ForeignKey(Pencil, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_text = models.TextField()
    # published date will be right now.
    comment_published_date = models.DateTimeField(default=timezone.localtime(timezone.now()))

    # to make the date in admin has the "Published date" column label
    def published_date(self):
        return self.comment_published_date

    # we only return the text up to 25 chars to make the column cleaner
    def __str__(self):
        return self.comment_text[:25]