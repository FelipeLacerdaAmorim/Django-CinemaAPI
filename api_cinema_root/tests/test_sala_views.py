from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Sala
from ..serializers import SalaSerializer

class SalasApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sala_data = {'sala_num': '101', 'sala_descricao': 'Sala de Projeção'}
        self.sala = Sala.objects.create(**self.sala_data)

    def test_get_salas(self):
        response = self.client.get(reverse('get_all_salas'))
        salas = Sala.objects.all()
        serializer = SalaSerializer(salas, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_by_num(self):
        response = self.client.get(reverse('get_salas_by_num', kwargs={'num': self.sala.sala_num}))
        serializer = SalaSerializer(self.sala)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_sala(self):
        valid_data = {'sala_num': '102', 'sala_descricao': 'Sala de Conferências'}
        response = self.client.post(reverse('post_sala'), data=valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_sala(self):
        updated_data = {'sala_num': self.sala.sala_num, 'sala_descricao': 'Sala de Reunião'}
        response = self.client.put(reverse('put_sala'), data=updated_data, format='json')
        updated_sala = Sala.objects.get(sala_num=self.sala.sala_num)
        serializer = SalaSerializer(updated_sala)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)

    def test_delete_sala(self):
        response = self.client.delete(reverse('delete_sala', kwargs={'num': self.sala.sala_num}))
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)