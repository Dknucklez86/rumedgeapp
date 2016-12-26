from django.contrib import admin

from .models import User

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'firstName', 'lastName', 'description']

admin.site.register(User)

# Register your models here.
