from django.test import TestCase
from ..models import Sala, SalaFilme, Filme
from ..serializers import SalaSerializer, SalaFilmeSerializer, FilmeSerializer

class SalaSerializerTest(TestCase):
    def setUp(self):
        self.sala_data = {'sala_num': 101, 'sala_descricao': 'Sala de Teste'}
        self.sala_serializer = SalaSerializer(data=self.sala_data)

    def test_sala_serializer_with_valid_data(self):
        self.assertTrue(self.sala_serializer.is_valid())
    
    def test_sala_serializer_with_invalid_data(self):
        sala_data_invalid = {'sala_descricao': 'Sala de Teste'}
        sala_serializer_invalid = SalaSerializer(data=sala_data_invalid)
        self.assertFalse(sala_serializer_invalid.is_valid())

class SalaFilmeSerializerTest(TestCase):
    def setUp(self):
        self.sala = Sala.objects.create(sala_num=101, sala_descricao='Sala de Teste')
        self.filme = Filme.objects.create(filme_nome='Filme de Teste', filme_diretor='Diretor Teste', filme_duracao='120 min')
        self.sala_filme_data = {'sala': self.sala.pk, 'filme': self.filme.pk}
        self.sala_filme_serializer = SalaFilmeSerializer(data=self.sala_filme_data)

    def test_sala_filme_serializer_with_valid_data(self):
        self.assertTrue(self.sala_filme_serializer.is_valid())
    
    def test_sala_filme_serializer_with_invalid_data(self):
        sala_filme_data_invalid = {'sala': 999, 'filme': 999}  # Sala e filme com IDs inválidos
        sala_filme_serializer_invalid = SalaFilmeSerializer(data=sala_filme_data_invalid)
        self.assertFalse(sala_filme_serializer_invalid.is_valid())

class FilmeSerializerTest(TestCase):
    def setUp(self):
        self.filme_data = {'filme_nome': 'Filme de Teste', 'filme_diretor': 'Diretor Teste', 'filme_duracao': '120 min'}
        self.filme_serializer = FilmeSerializer(data=self.filme_data)

    def test_filme_serializer_with_valid_data(self):
        self.assertTrue(self.filme_serializer.is_valid())
    
    def test_filme_serializer_with_invalid_data(self):
        filme_data_invalid = {'filme_diretor': 'Diretor Teste', 'filme_duracaoo': ''}  # Nome do filme não fornecido
        filme_serializer_invalid = FilmeSerializer(data=filme_data_invalid)
        self.assertTrue(filme_serializer_invalid.is_valid())