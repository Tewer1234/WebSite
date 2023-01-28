from django.contrib import admin
from django.urls import path,include    
from web_tool import views
urlpatterns = [
    path("index/",views.index),
    path("index2/",views.index2),
    path("pag/",views.pag),
    path("browse_data/",views.browse_data),
    path("ajax_data2/",views.ajax_data2),
    path("ajax_data/",views.ajax_data),
    path("readCSV/",views.readCSV),
]
    