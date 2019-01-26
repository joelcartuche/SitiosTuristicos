from rest_framework import routers, serializers, viewsets
from app.Cantones.models import Cantones
from rest_framework.views import APIView


class cantonesSerializable(serializers.ModelSerializer):
    class Meta:
        model= Cantones
        fields= ("codigo","nombre","latitud","longitud","descripcion","imagen")