from django.urls import path
from .views import ArchivoCreateAPIView, ArchivoUpdateAPIView, ArchivoDeleteAPIView, ArchivoList, AutorList, AutorCreateAPIView, AutorDeleteAPIView, AutorUpdateAPIView
urlpatterns = [
    path("book/list/", ArchivoList.as_view(), name="listar_archivo"),
    path("book/create/", ArchivoCreateAPIView.as_view(), name="crear_archivo"),
    path("book/update/<int:pk>", ArchivoUpdateAPIView.as_view(),
         name="actualizar_archivo"),
    path("book/delete/<int:pk>", ArchivoDeleteAPIView.as_view(),
         name="eliminar_archivo"),

    path("autor/list/", AutorList.as_view(), name="listar_Autor"),
    path("autor/create/", AutorCreateAPIView.as_view(), name="crear_Autor"),
    path("autor/update/<int:pk>", AutorUpdateAPIView.as_view(),
         name="actualizar_Autor"),
    path("autor/delete/<int:pk>",
         AutorDeleteAPIView.as_view(), name="eliminar_Autor"),


]
