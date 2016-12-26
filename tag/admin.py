# -*- coding: utf-8 -*-


from django.contrib import admin
from tag.models import Tag, Unit, FieldType


# Register your models here.
admin.site.register(Tag)
admin.site.register(Unit)
admin.site.register(FieldType)
