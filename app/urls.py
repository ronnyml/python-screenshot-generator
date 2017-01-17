# -*- encoding: utf-8 -*-

from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^get_screenshot', views.get_screenshot, name="get_screenshot"),
]