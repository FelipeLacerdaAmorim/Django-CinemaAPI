from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Filme
from ..serializers import FilmeSerializer

class FilmesApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.filme_data = {'filme_nome': 'Filme Teste', 'filme_diretor': 'Diretor Teste', 'filme_duracao': '120 min'}
        self.filme = Filme.objects.create(**self.filme_data)

    def test_get_filmes(self):
        response = self.client.get(reverse('get_all_filmes'))
        filmes = Filme.objects.all()
        serializer = FilmeSerializer(filmes, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_by_id(self):
        response = self.client.get(reverse('get_filmes_by_num', kwargs={'id': self.filme.id}))
        serializer = FilmeSerializer(self.filme)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_filme(self):
        response = self.client.post(reverse('post_filme'), data=self.filme_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_filme(self):
        updated_data = {'id': self.filme.id, 'filme_nome': 'Filme Atualizado', 'filme_diretor': 'Novo Diretor', 'filme_duracao': '90 min'}
        response = self.client.put(reverse('put_filme'), data=updated_data, format='json')
        updated_filme = Filme.objects.get(id=self.filme.id)
        serializer = FilmeSerializer(updated_filme)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)

    def test_delete_filme(self):
        response = self.client.delete(reverse('delete_filme', kwargs={'id': self.filme.id}))
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)