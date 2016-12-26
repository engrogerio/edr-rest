# -*- coding: utf-8 -*-

from django.db.models import UUIDField, CharField, ForeignKey, IntegerField, DecimalField
import uuid
from django.core.urlresolvers import reverse
from edr.models import EdrModel

# Create your models here.


class FieldType(EdrModel):
    name = CharField(max_length=20)

    def __str__(self):
        return self.name


class Unit(EdrModel):
    name = CharField(max_length=25)
    symbol = CharField(max_length=10, null=True, blank=True)
    unit_of = CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name+' ( '+self.symbol+' )'


class Tag(EdrModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=255)
    type = ForeignKey(FieldType)
    unit = ForeignKey(Unit)
    decimal_places = IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('list')

    def __str__(self):
        return self.name+' ( '+self.unit.symbol+' )'


class Value(EdrModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = ForeignKey(Tag)
    numeric = DecimalField(decimal_places=10, max_digits=20, blank=True, null=True)
    text = CharField(max_length=1000, blank=True, null=True)
    inspection =  ForeignKey('form.Inspection')