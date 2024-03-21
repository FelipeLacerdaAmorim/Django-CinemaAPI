from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework import status

from ..models import SalaFilme
from ..serializers import SalaFilmeSerializer

import json


@api_view(['GET'])
def get_sala_filmes(request):
    if request.method == 'GET':
        safis = SalaFilme.objects.all()

        serializer = SalaFilmeSerializer(safis, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'sala': openapi.Schema(type=openapi.TYPE_STRING),
        'filme': openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=['sala', 'filme'] 
))
@api_view(['POST'])
def post_sala_filme(request):
 if request.method == 'POST':
        nova_sala_filme = request.data

        serializer = SalaFilmeSerializer(data=nova_sala_filme)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_STRING),
        'sala': openapi.Schema(type=openapi.TYPE_STRING),
        'filme': openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=['sala', 'filme'] 
))
@api_view(['PUT'])
def put_sala_filme(request):
    if request.method == 'PUT':
        
        sala_filme = request.data['id']

        update_sala_filme = SalaFilme.objects.get(id=sala_filme)
        
        serializer = SalaFilmeSerializer(update_sala_filme, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_sala_filme(request, id):
    if request.method == 'DELETE':
        try:
            sala_filme = SalaFilme.objects.get(id=id)
            sala_filme.delete()

            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)