from django.urls import path

from . import views 

urlpatterns = [
    path('', views.get_fields, name='index'),
    path('download', views.download, name='download')
]