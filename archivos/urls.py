from django.urls import path
from .views import ArchivoList, ArchivoListDetail

urlpatterns=[
    path("archivo/",ArchivoList.as_view() ,name="archivos"),
    path("archivo/<int:pk>",ArchivoListDetail.as_view(),name="detail"),
    ]