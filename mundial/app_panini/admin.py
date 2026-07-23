from django.contrib import admin
from .models import Country, Team, Player

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'confederation', 'flag_image')
    list_filter = ('confederation',)
    search_fields = ('name', 'code')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'group', 'badge_image')
    list_filter = ('group', 'country__confederation')
    search_fields = ('name', 'country__name')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'jersey_number', 'position', 'team', 'player_image')
    list_filter = ('position', 'team__group', 'team__country__confederation')
    search_fields = ('name', 'team__name')
    ordering = ('team', 'jersey_number')