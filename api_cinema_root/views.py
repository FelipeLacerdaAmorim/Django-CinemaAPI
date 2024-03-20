from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework import status

from .models import Sala, SalaFilme, Filme
from .serializers import SalaSerializer, SalaFilmeSerializer, FilmeSerializer

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
    

## Filmes



@api_view(['GET'])
def get_filmes(request):
    if request.method == 'GET':
        filmes = Filme.objects.all()

        serializer = FilmeSerializer(filmes, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_by_id(request, id):
    
    try:
        filme = Filme.objects.get(id=id)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FilmeSerializer(filme)
        return Response(serializer.data)
    

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'filme_nome': openapi.Schema(type=openapi.TYPE_STRING),
        'filme_diretor': openapi.Schema(type=openapi.TYPE_STRING),
        'filme_duracao': openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=['id', 'filme_nome', 'filme_diretor', 'filme_duracao'] 
))
@api_view(['POST'])
def post_filme(request):
 if request.method == 'POST':
        novo_filme = request.data

        serializer = FilmeSerializer(data=novo_filme)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_STRING),
        'filme_nome': openapi.Schema(type=openapi.TYPE_STRING),
        'filme_diretor': openapi.Schema(type=openapi.TYPE_STRING),
        'filme_duracao': openapi.Schema(type=openapi.TYPE_STRING),
    },
    required=['id', 'filme_nome', 'filme_diretor', 'filme_duracao'] 
))
@api_view(['PUT'])
def put_filme(request):
    if request.method == 'PUT':
        
        filme = request.data['id']

        update_filme = Filme.objects.get(id=filme)
        
        serializer = FilmeSerializer(update_filme, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_filme(request, id):
    if request.method == 'DELETE':
        try:
            filme = Filme.objects.get(id=id)
            filme.delete()

            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        


# Sala-Filme
        
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