from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), #Pantalla de Pokemons
    path("<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("trainer/<int:trainer_id>/", views.trainer_detail, name="trainer"),
    
]