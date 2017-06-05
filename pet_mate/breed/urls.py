from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^get-breed/', views.scrap_breed, name='get-breed' )
]
