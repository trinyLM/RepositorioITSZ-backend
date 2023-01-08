from rest_framework import serializers
from .models import Archivo,Autor,Campus,Carrera


class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        fields ="__all__"



class AutorSerializer(serializers.ModelSerializer):
    archivos= serializers.StringRelatedField(many= True)

    
    class Meta:
        model = Autor
        fields = "__all__"
    def to_representation(self,instance):
        changes = super().to_representation(instance)
        id_carrera = changes["carrera"]
        buscar_nombre_carrera = Carrera.objects.get(id=id_carrera)
        changes["carrera"] = buscar_nombre_carrera.nombre

        id_campus = changes["campus"]
        buscar_nombre_campus = Campus.objects.get(id=id_campus)
        changes["campus"] = buscar_nombre_campus.nombre
        return changes 
  
