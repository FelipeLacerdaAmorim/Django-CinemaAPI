from django.contrib import admin
from django.urls import path, include

#from . import views
from .views.sala import get_salas, get_by_num, post_sala, put_sala, delete_sala
from .views.filme import get_filmes, get_by_id, post_filme, put_filme, delete_filme
from .views.salafilme import get_sala_filmes, post_sala_filme, put_sala_filme, delete_sala_filme


urlpatterns = [
    path('sala', get_salas, name='get_all_salas'),
    path('sala/<str:num>', get_by_num, name='get_salas_by_num'),
    path('sala/test/post', post_sala, name='post_sala'),
    path('sala/test/put', put_sala, name='put_sala'),
    path('sala/test/delete/<str:num>', delete_sala, name='delete_sala'),

    path('filme', get_filmes, name='get_all_filmes'),
    path('filme/<str:id>', get_by_id, name='get_filmes_by_num'),
    path('filme/test/post', post_filme, name='post_filme'),
    path('filme/test/put', put_filme, name='put_filme'),
    path('filme/test/delete/<str:id>', delete_filme, name='delete_filme'),

    path('salafilme', get_sala_filmes, name='get_all_sala_filmes'),
    path('salafilme/test/post', post_sala_filme, name='post_sala_filme'),
    path('salafilme/test/put', put_sala_filme, name='put_sala_filme'),
    path('salafilme/test/delete/<str:id>', delete_sala_filme, name='delete_sala_filme'),
]
