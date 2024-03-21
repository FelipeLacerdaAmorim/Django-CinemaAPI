from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from rest_framework import status

from ..models import Filme
from ..serializers import FilmeSerializer

import json


        # if return_salas == True:
        #     filmes_data = []
        #     for filme in filmes:
        #         salas = filme.salafilme_set.all()
        #         salas_data = [{'id': sala.id, 'nome': sala.nome} for sala in salas]
        #         filme_data = {
        #             'id': filme.id,
        #             'nome': filme.nome,
        #             'salas': salas_data
        #         }
        #         filmes_data.append(filme_data)


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
        
