# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
from tag.models import Tag, Unit
from tag.forms import ContactForm, TagForm


# Create your views here.
class TagListView(ListView):
    model = Tag
    template_name_suffix = '_view_form'


class TagCreateView(CreateView):
    model = Tag
    fields = '__all__'
    template_name_suffix = '_create_form'


class TagUpdateView(UpdateView):
    form = TagForm
    model = Tag
    fields = '__all__'
    template_name_suffix = '_update_form'
    slug_field = 'id'


class TagDeleteView(DeleteView):
    model = Tag
    template_name_suffix = '_delete_form'
    slug_field = 'id'


from rest_framework import authentication, permissions, viewsets
from .models import Value, Tag, FieldType, Unit
from .serializers import ValueSerializer, TagSerializer, FieldTypeSerializer, UnitSerializer


class DefaultMixin(object):
    """
    Configurações default para autenticação, permissões,
    filtragem e paginação da view
    """

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class TagViewSet(DefaultMixin,viewsets.ModelViewSet):
    """
    Endpoint da API para listar e criar Inspections
    """

    queryset = Tag.objects.all() #order_by('form__name')
    serializer_class = TagSerializer


class FieldTypeViewSet(DefaultMixin,viewsets.ModelViewSet):
    """
    Endpoint da API para listar e criar Inspections
    """

    queryset = FieldType.objects.order_by('name')
    serializer_class = FieldTypeSerializer


class UnitViewSet(DefaultMixin,viewsets.ModelViewSet):
    """
    Endpoint da API para listar e criar Inspections
    """

    queryset = Unit.objects.order_by('name')
    serializer_class = UnitSerializer


class ValueViewSet(DefaultMixin,viewsets.ModelViewSet):
    """
    Endpoint da API para listar e criar Inspections
    """

    queryset = Value.objects.all()
    serializer_class = ValueSerializer
