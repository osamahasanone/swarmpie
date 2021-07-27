from django.contrib import admin
from .models import *


class VerbAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    list_display = ('id', 'name', 'description')
    ordering = ['id']


admin.site.register(Verb, VerbAdmin)
