from django.contrib import admin

# Register your models here.

from .models import Review, Like

admin.site.register(Review)
admin.site.register(Like)
