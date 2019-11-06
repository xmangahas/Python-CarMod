from django.contrib import admin
from .models import Car, Category, Part

# Register your models here.
admin.site.register(Car)
admin.site.register(Category)
admin.site.register(Part)