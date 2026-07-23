from django.db import models

class Country(models.Model):
    CONFEDERATION_CHOICES = [
        ('UEFA', 'UEFA - Europe'),
        ('CONMEBOL', 'CONMEBOL - South America'),
        ('CONCACAF', 'CONCACAF - North America'),
        ('CAF', 'CAF - Africa'),
        ('AFC', 'AFC - Asia'),
        ('OFC', 'OFC - Oceania'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=2, unique=True)  # ISO 2-letter country code
    confederation = models.CharField(max_length=10, choices=CONFEDERATION_CHOICES)
    flag_image = models.ImageField(upload_to='flags/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class Team(models.Model):
    GROUP_CHOICES = [
        ('A', 'Group A'), ('B', 'Group B'), ('C', 'Group C'), 
        ('D', 'Group D'), ('E', 'Group E'), ('F', 'Group F'),
        ('G', 'Group G'), ('H', 'Group H'), ('I', 'Group I'),
        ('J', 'Group J'), ('K', 'Group K'), ('L', 'Group L'),
    ]
    
    name = models.CharField(max_length=100)
    country = models.OneToOneField(Country, on_delete=models.CASCADE, related_name='team')
    group = models.CharField(max_length=1, choices=GROUP_CHOICES)
    badge_image = models.ImageField(upload_to='badges/', blank=True, null=True)
    ranking = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['group', 'name']
    
    def __str__(self):
        return f"{self.name} - Group {self.group}"

class Player(models.Model):
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ]
    
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    jersey_number = models.IntegerField()
    age = models.IntegerField(blank=True, null=True)
    player_image = models.ImageField(upload_to='players/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['team', 'jersey_number']
        unique_together = ['team', 'jersey_number']
    
    def __str__(self):
        return f"{self.name} #{self.jersey_number} ({self.team.name})"