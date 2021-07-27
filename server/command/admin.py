from django.contrib import admin
from .models import *


class VerbParameterAdmin(admin.ModelAdmin):
    fields = ('verb', 'order')
    list_display = ('id', 'verb', 'order')
    ordering = ['id']


class VerbParameterChoiceAdmin(admin.ModelAdmin):
    fields = ('verb_parameter', 'header', 'value', 'description')
    list_display = ('id', 'verb_parameter', 'header', 'value', 'description')
    ordering = ['id']


class CommandAdmin(admin.ModelAdmin):
    fields = ('verb',)
    list_display = ('id', 'verb', 'ts')
    ordering = ['id']


class CommandParameterAdmin(admin.ModelAdmin):
    fields = ('command', 'verb_parameter', 'value')
    list_display = ('id', 'command', 'verb_parameter', 'value')
    ordering = ['id']


admin.site.register(VerbParameter, VerbParameterAdmin)
admin.site.register(VerbParameterChoice, VerbParameterChoiceAdmin)
admin.site.register(Command, CommandAdmin)
admin.site.register(CommandParameter, CommandParameterAdmin)
