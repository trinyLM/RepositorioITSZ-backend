
from rest_framework import generics
from .models import Archivo
from .serializers import ArchivoSerializer
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class ArchivoList(generics.ListAPIView):
    """Vista que lista todos los archivos"""
    # AUTENTICACION
    #permission_classes = [IsAuthenticated]
    # queryset
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo', 'materia', 'fecha_publicacion','tipo_de_publicacion']


class ArchivoListDetail(generics.RetrieveAPIView):

    # AUTENTICACION
    #permission_classes = [IsAuthenticated]
    # queryset
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo', 'materia', 'fecha_publicacion']
