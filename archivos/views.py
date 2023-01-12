from rest_framework import filters
from rest_framework import generics
from .models import Archivo,Autor
from .serializers import ArchivoSerializer,AutorSerializer
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class ArchivoList(generics.ListAPIView):
    """Vista que lista todos los archivos"""
    # AUTENTICACION
    permission_classes = [IsAuthenticated]
    # queryset
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo', 'materia','autor__nombres','tipo_de_publicacion__nombre','fecha_publicacion','resumen']
    
    
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['titulo', 'materia', 'fecha_publicacion','tipo_de_publicacion']


class ArchivoListDetail(generics.RetrieveAPIView):

    # AUTENTICACION
    permission_classes = [IsAuthenticated]
    # queryset
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo', 'materia', 'fecha_publicacion']



class AutorList(generics.ListAPIView):
    
    permission_classes =[IsAuthenticated]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    def get_queryset(self):
        id=1
        return Autor.objects.filter(id=id)


class AutorListDetail(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer





