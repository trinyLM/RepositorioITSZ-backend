from rest_framework import filters
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from archivos.models import Archivo, Autor
from archivos.pagination import CustomPagination
from archivos.serializers import ArchivoSerializer, AutorSerializer


class ArchivoList(ListAPIView):
    """Vista que lista todos los archivos"""
    # AUTENTICACION
    permission_classes = [IsAuthenticated, IsAdminUser]
    # queryset
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'materia', 'autor__nombres',
                     'tipo_de_publicacion__nombre', 'fecha_publicacion', 'resumen']


class ArchivoListDetail(RetrieveAPIView):

    # AUTENTICACION
    permission_classes = [IsAuthenticated, IsAdminUser]
    # queryset
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer


class ArchivoCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer


class ArchivoUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer


class ArchivoDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer


class AutorList(ListAPIView):
    """Vista que lista todos los archivos"""
    # AUTENTICACION
    permission_classes = [IsAuthenticated, IsAdminUser]
    # queryset
    queryset = Autor.objects.all()
    serializer_class = ArchivoSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', ]


class AutorListDetail(RetrieveAPIView):

    # AUTENTICACION
    permission_classes = [IsAuthenticated, IsAdminUser]
    # queryset
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class AutorCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class AutorUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class AutorDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
