# -*- coding: utf-8 -*-


from django.contrib import admin
from form.models import Form, Inspection

# Register your models here.

class FormAdmin(admin.ModelAdmin):
    filter_horizontal=('tag',)

admin.site.register(Form, FormAdmin)
admin.site.register(Inspection)
