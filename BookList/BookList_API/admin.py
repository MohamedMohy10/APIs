from django.contrib import admin
from .models import Book, Inventory

# Register your models here.
admin.site.register(Book)
admin.site.register(Inventory)