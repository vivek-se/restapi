from django.contrib import admin
from .models import library, student

# Register your models here.

admin.site.register(library)

admin.site.register(student)