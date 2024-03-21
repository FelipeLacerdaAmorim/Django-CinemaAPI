from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from ..models import Sala, Filme, SalaFilme

class SalaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Sala.objects.create(sala_num=101, sala_descricao='Sala 1')

    def test_sala_num_label(self):
        sala = Sala.objects.get(sala_num=101)
        field_label = sala._meta.get_field('sala_num').verbose_name
        self.assertEqual(field_label, 'sala num')

    def test_sala_descricao_max_length(self):
        sala = Sala.objects.get(sala_num=101)
        max_length = sala._meta.get_field('sala_descricao').max_length
        self.assertEqual(max_length, 200)

class FilmeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Filme.objects.create(filme_nome='Filme Teste', filme_diretor='Diretor Teste', filme_duracao='120 min')

    def test_filme_nome_label(self):
        filme = Filme.objects.get(filme_nome='Filme Teste')
        field_label = filme._meta.get_field('filme_nome').verbose_name
        self.assertEqual(field_label, 'filme nome')

    def test_filme_diretor_label(self):
        filme = Filme.objects.get(filme_nome='Filme Teste')
        field_label = filme._meta.get_field('filme_diretor').verbose_name
        self.assertEqual(field_label, 'filme diretor')

    def test_filme_duracao_max_length(self):
        filme = Filme.objects.get(filme_nome='Filme Teste')
        max_length = filme._meta.get_field('filme_duracao').max_length
        self.assertEqual(max_length, 10)

class SalaFilmeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        sala = Sala.objects.create(sala_num=101, sala_descricao='Sala 1')
        filme = Filme.objects.create(filme_nome='Filme Teste', filme_diretor='Diretor Teste', filme_duracao='120 min')
        SalaFilme.objects.create(sala=sala, filme=filme)

    def test_sala_filme_relation(self):
        sala_filme = SalaFilme.objects.get(sala__sala_num=101)
        self.assertEqual(sala_filme.sala.sala_num, 101)
        self.assertEqual(sala_filme.filme.filme_nome, 'Filme Teste')