"""Defines URL patterns for biorbyt_products."""

from django.conf.urls import include, url
from django.contrib.auth.models import Group, User
from django.contrib.auth.views import login

from . import views


# URL Patterns for the site pages
urlpatterns = [

    url(r'^$', views.index, name='index'),
]
