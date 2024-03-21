from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework import status

from ..models import Sala
from ..serializers import SalaSerializer

import json


@api_view(['GET'])
def get_salas(request):
    if request.method == 'GET':
        salas = Sala.objects.all()

        serializer = SalaSerializer(salas, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_by_num(request, num):
    
    try:
        sala = Sala.objects.get(sala_num=num)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SalaSerializer(sala)
        return Response(serializer.data)
    

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'sala_num': openapi.Schema(type=openapi.TYPE_STRING),
        'sala_descricao': openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=['sala_num', 'sala_descricao'] 
))
@api_view(['POST'])
def post_sala(request):
    if request.method == 'POST':
        nova_sala = request.data

        serializer = SalaSerializer(data=nova_sala)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'sala_num': openapi.Schema(type=openapi.TYPE_STRING),
        'sala_descricao': openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=['sala_num', 'sala_descricao'] 
))
@api_view(['PUT'])
def put_sala(request):
    if request.method == 'PUT':
        
        sala = request.data['sala_num']

        update_sala = Sala.objects.get(sala_num=sala)
        
        serializer = SalaSerializer(update_sala, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_sala(request, num):
    if request.method == 'DELETE':
        try:
            sala = Sala.objects.get(sala_num=num)
            sala.delete()

            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)