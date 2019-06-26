# -*- encoding: utf-8 -*-

from django.urls import include, path
from django.views.generic import TemplateView
from app import views

urlpatterns = [
    path('', views.get_screenshot, name='get_screenshot'),
]