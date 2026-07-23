from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Country, Team, Player

def countries_view(request):
    """Display all countries with their flags and teams"""
    countries = Country.objects.select_related('team').all()
    
    context = {
        'countries': countries,
        'title': 'Panini Mundial 2026'
    }
    return render(request, 'app_panini/paises.html', context)

def country_players_view(request, country_code):
    """Display players for a specific country"""
    country = get_object_or_404(Country, code=country_code)
    team = getattr(country, 'team', None)
    players = team.players.all() if team else []
    
    context = {
        'country': country,
        'team': team,
        'players': players,
        'title': f'Jugadores de {country.name}'
    }
    return render(request, 'app_panini/country_players.html', context)

def players_view(request):
    """Display all players"""
    players = Player.objects.select_related('team__country').all()
    
    context = {
        'players': players,
        'title': 'Jugadores Mundial 2026'
    }
    return render(request, 'app_panini/players.html', context)

def teams_by_group_view(request):
    """API endpoint to get teams organized by groups"""
    teams_by_group = {}
    
    for group_code, group_name in Team.GROUP_CHOICES:
        teams = Team.objects.filter(group=group_code).select_related('country')
        teams_by_group[group_code] = [
            {
                'name': team.name,
                'country': team.country.name,
                'country_code': team.country.code,
                'flag': team.country.flag_image.url if team.country.flag_image else None,
                'badge': team.badge_image.url if team.badge_image else None,
                'confederation': team.country.confederation
            }
            for team in teams
        ]
    
    return JsonResponse(teams_by_group)

def teams_by_confederation_view(request):
    """API endpoint to get teams organized by confederation"""
    teams_by_conf = {}
    
    for conf_code, conf_name in Country.CONFEDERATION_CHOICES:
        countries = Country.objects.filter(confederation=conf_code).select_related('team')
        teams_by_conf[conf_code] = [
            {
                'name': country.team.name if hasattr(country, 'team') else country.name,
                'country': country.name,
                'country_code': country.code,
                'flag': country.flag_image.url if country.flag_image else None,
                'badge': country.team.badge_image.url if hasattr(country, 'team') and country.team.badge_image else None,
                'group': country.team.group if hasattr(country, 'team') else None
            }
            for country in countries
        ]
    
    return JsonResponse(teams_by_conf)

def players_by_team_view(request):
    """API endpoint to get players organized by team"""
    players_by_team = {}
    
    teams = Team.objects.all()
    for team in teams:
        players = team.players.all()
        players_by_team[team.name] = [
            {
                'name': player.name,
                'jersey_number': player.jersey_number,
                'position': player.position,
                'age': player.age,
                'image': player.player_image.url if player.player_image else None
            }
            for player in players
        ]
    
    return JsonResponse(players_by_team)