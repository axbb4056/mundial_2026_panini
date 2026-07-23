from django.core.management.base import BaseCommand
from app_panini.models import Country, Team, Player

class Command(BaseCommand):
    help = 'Load FIFA World Cup 2026 teams, countries and sample players data'

    def handle(self, *args, **options):
        # Simple 10 teams for testing (using 2-letter ISO codes)
        world_cup_data = [
            {'name': 'Ecuador', 'code': 'EC', 'conf': 'CONMEBOL', 'group': 'A'},
            {'name': 'Canada', 'code': 'CA', 'conf': 'CONCACAF', 'group': 'A'},
            {'name': 'Japan', 'code': 'JP', 'conf': 'AFC', 'group': 'B'},
            {'name': 'South Korea', 'code': 'KR', 'conf': 'AFC', 'group': 'B'},
            {'name': 'Argentina', 'code': 'AR', 'conf': 'CONMEBOL', 'group': 'C'},
            {'name': 'Brazil', 'code': 'BR', 'conf': 'CONMEBOL', 'group': 'C'},
            {'name': 'Germany', 'code': 'DE', 'conf': 'UEFA', 'group': 'D'},
            {'name': 'France', 'code': 'FR', 'conf': 'UEFA', 'group': 'D'},
            {'name': 'United States', 'code': 'US', 'conf': 'CONCACAF', 'group': 'E'},
            {'name': 'Mexico', 'code': 'MX', 'conf': 'CONCACAF', 'group': 'E'},
        ]
        
        self.stdout.write('Creating countries and teams...')
        
        for data in world_cup_data:
            # Create or get country
            country, created = Country.objects.get_or_create(
                code=data['code'],
                defaults={
                    'name': data['name'],
                    'confederation': data['conf'],
                }
            )
            
            if created:
                self.stdout.write(f'Created country: {country.name}')
            
            # Create team if it doesn't exist
            team, team_created = Team.objects.get_or_create(
                country=country,
                defaults={
                    'name': data['name'],
                    'group': data['group'],
                }
            )
            
            if team_created:
                self.stdout.write(f'Created team: {team.name} - Group {team.group}')
        
        # Add sample players for some teams
        sample_players = [
            # Ecuador
            {'name': 'Enner Valencia', 'team_code': 'EC', 'number': 13, 'position': 'FWD', 'age': 34},
            {'name': 'Alexander Domínguez', 'team_code': 'EC', 'number': 22, 'position': 'GK', 'age': 37},
            
            # Argentina  
            {'name': 'Lionel Messi', 'team_code': 'AR', 'number': 10, 'position': 'FWD', 'age': 37},
            {'name': 'Emiliano Martínez', 'team_code': 'AR', 'number': 23, 'position': 'GK', 'age': 31},
            
            # Brazil
            {'name': 'Vinícius Jr.', 'team_code': 'BR', 'number': 7, 'position': 'FWD', 'age': 24},
            {'name': 'Alisson', 'team_code': 'BR', 'number': 1, 'position': 'GK', 'age': 31},
        ]
        
        self.stdout.write('Creating sample players...')
        
        for player_data in sample_players:
            try:
                country = Country.objects.get(code=player_data['team_code'])
                team = country.team
                
                player, created = Player.objects.get_or_create(
                    team=team,
                    jersey_number=player_data['number'],
                    defaults={
                        'name': player_data['name'],
                        'position': player_data['position'],
                        'age': player_data['age'],
                    }
                )
                
                if created:
                    self.stdout.write(f'Created player: {player.name} #{player.jersey_number}')
                    
            except Country.DoesNotExist:
                self.stdout.write(f'Country {player_data["team_code"]} not found')
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(world_cup_data)} teams and sample players!')
        )