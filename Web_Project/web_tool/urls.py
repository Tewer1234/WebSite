from django.contrib import admin
from django.urls import path,include    
from web_tool import views
urlpatterns = [
    path("index/",views.index),
    path("pag/",views.pag),
    path("ajax_data/",views.ajax_data),
]
    