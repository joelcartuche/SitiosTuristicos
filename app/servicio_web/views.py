from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from app.Cantones.models import Cantones
from .serializable import cantonesSerializable
from rest_framework.views import APIView
from rest_framework.response import Response


class listaCantones(APIView):
    def get(self,request):
        owner = serializers.Field()
        lista = Cantones.objects.all()
        objetoSerializable = cantonesSerializable(lista,many = True)
        return Response(objetoSerializable.data)