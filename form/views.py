# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
from form.models import Form


# Create your views here.
class FormListView(ListView):
    model = Form
    template_name_suffix = '_view_form'


class FormCreateView(CreateView):
    model = Form
    fields = '__all__'
    template_name_suffix = '_create_form'


class FormUpdateView(UpdateView):
    model = Form
    fields = '__all__'
    template_name_suffix = '_update_form'
    slug_field = 'id'


class FormDeleteView(DeleteView):
    model = Form
    template_name_suffix = '_delete_form'
    slug_field = 'id'


from rest_framework import authentication, permissions, viewsets
from .models import Inspection
from .serializers import InspectionSerializer, FormSerializer


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


class InspectionViewSet(DefaultMixin,viewsets.ModelViewSet):
    """
    Endpoint da API para listar e criar Inspections
    """

    queryset = Inspection.objects.all() #order_by('form__name')
    serializer_class = InspectionSerializer


class FormViewSet(DefaultMixin,viewsets.ModelViewSet):
    """
    Endpoint da API para listar e criar Inspections
    """

    queryset = Form.objects.order_by('name')
    serializer_class = FormSerializer
