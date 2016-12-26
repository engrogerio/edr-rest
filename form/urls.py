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
# from django.conf.urls import url
# from django.contrib import admin
# from form.views import FormListView, FormCreateView, FormUpdateView, FormDeleteView
from rest_framework.routers import DefaultRouter
from form.views import InspectionViewSet, FormViewSet

router = DefaultRouter()
router.register(r'tags', InspectionViewSet)
router.register(r'forms', FormViewSet)

urlpatterns = [
    # url(r'^$', FormListView.as_view(), name='list_form'),
    # url(r'^create/', FormCreateView.as_view(), name='create_form'),
    # url(r'^update/(?P<slug>[^/]+)/$', FormUpdateView.as_view(), name='update_form'),
    # url(r'^delete/(?P<slug>[^/]+)/$', FormDeleteView.as_view(), name='delete_form'),

]
