from django.urls import path
from . import views

app_name = 'app_panini'

urlpatterns = [
    path('', views.countries_view, name='countries'),
    path('paises/', views.countries_view, name='paises'),
    path('country/<str:country_code>/players/', views.country_players_view, name='country_players'),
    path('players/', views.players_view, name='players'),
    path('api/teams-by-group/', views.teams_by_group_view, name='teams_by_group'),
    path('api/teams-by-confederation/', views.teams_by_confederation_view, name='teams_by_confederation'),
    path('api/players-by-team/', views.players_by_team_view, name='players_by_team'),
]