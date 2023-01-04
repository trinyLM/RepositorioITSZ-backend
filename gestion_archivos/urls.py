from django.urls import path
from .views import ArchivoCreateAPIView,ArchivoUpdateAPIView,ArchivoDeleteAPIView
urlpatterns =[
    path("create/",ArchivoCreateAPIView.as_view(),name="crear_archivo"),
    path("update/<int:pk>",ArchivoUpdateAPIView.as_view(),name="actualizar_archivo"),
    path("delete/<int:pk>",ArchivoDeleteAPIView.as_view(),name="eliminar_archivo"),


]