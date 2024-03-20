from django.db import models

# Create your models here.
class Sala(models.Model):
    sala_num = models.IntegerField(primary_key=True)
    sala_descricao = models.CharField(max_length=200, default='')

    def __str__(self):
        return f'(Sala número {self.sala_num}: {self.sala_descricao})'


class Filme(models.Model):
    filme_nome = models.CharField(max_length=60, default='')
    filme_diretor = models.CharField(max_length=60, default='')
    filme_duracao = models.CharField(max_length=10, default='')

    def __str__(self):
        return f'(Filme "{self.filme_nome}" do diretor {self.filme_diretor} ({self.filme_duracao}))'
    
class SalaFilme(models.Model): 
    sala = models.ForeignKey(Sala, on_delete = models.CASCADE) 
    filme = models.ForeignKey(Filme, on_delete = models.CASCADE) 