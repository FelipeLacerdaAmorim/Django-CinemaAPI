from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('sala', views.get_salas, name='get_all_salas'),
    path('sala/<str:num>', views.get_by_num, name='get_salas_by_num'),
    path('sala/test/post', views.post_sala, name='post_sala'),
    path('sala/test/put', views.put_sala, name='put_sala'),
    path('sala/test/delete/<str:num>', views.delete_sala, name='delete_sala'),

    path('filme', views.get_filmes, name='get_all_filmes'),
    path('filme/<str:id>', views.get_by_id, name='get_filmes_by_num'),
    path('filme/test/post', views.post_filme, name='post_filme'),
    path('filme/test/put', views.put_filme, name='put_filme'),
    path('filme/test/delete/<str:id>', views.delete_filme, name='delete_filme'),

    path('salafilme', views.get_sala_filmes, name='get_all_sala_filmes'),
    path('salafilme/test/post', views.post_sala_filme, name='post_sala_filme'),
    path('salafilme/test/put', views.put_sala_filme, name='put_sala_filme'),
    path('salafilme/test/delete/<str:id>', views.delete_sala_filme, name='delete_sala_filme'),
]
