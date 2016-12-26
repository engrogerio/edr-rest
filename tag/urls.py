# -*- coding: utf-8 -*-


"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tag.models import Tag
from tag.views import TagCreateView, TagUpdateView, TagDeleteView, TagListView, \
    TagViewSet, FieldTypeViewSet, UnitViewSet, ValueViewSet
from form.views import InspectionViewSet, FormViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'field_types', FieldTypeViewSet)
router.register(r'units', UnitViewSet)
router.register(r'values', ValueViewSet)
router.register(r'inspections', InspectionViewSet)
router.register(r'forms', FormViewSet)



urlpatterns = [
    # url(r'^$', TagListView.as_view(), name='list'),
    # url(r'^create/', TagCreateView.as_view(), name='create'),
    # url(r'^update/(?P<slug>[^/]+)/$', TagUpdateView.as_view(), name='update'),
    # url(r'^delete/(?P<slug>[^/]+)/$', TagDeleteView.as_view(), name='delete'),
]
