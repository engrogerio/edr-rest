# -*- coding: utf-8 -*-

from django.db.models import ManyToManyField, ForeignKey, CharField, DateTimeField
from django.db.models import UUIDField
from tag.models import Tag
from edr.models import EdrModel
import uuid
from django.core.urlresolvers import reverse


# Create your models here.
class Form(EdrModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = ForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    name = CharField(max_length=255)
    tag = ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list')


class Inspection(EdrModel):
    form = ForeignKey(Form)

    def __str__(self):
        return self.form.name
