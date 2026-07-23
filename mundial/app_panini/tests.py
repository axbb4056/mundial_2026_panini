from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Country, Team, Player

class CountryModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(
            name="Ecuador",
            code="EC",
            confederation="CONMEBOL"
        )

    def test_country_creation(self):
        self.assertEqual(self.country.name, "Ecuador")
        self.assertEqual(self.country.code, "EC")
        self.assertEqual(str(self.country), "Ecuador (EC)")

class TeamModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(
            name="Ecuador",
            code="EC", 
            confederation="CONMEBOL"
        )
        self.team = Team.objects.create(
            name="Ecuador",
            country=self.country,
            group="A"
        )

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Ecuador")
        self.assertEqual(self.team.group, "A")
        self.assertEqual(str(self.team), "Ecuador - Group A")

class PlayerModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(
            name="Ecuador",
            code="EC",
            confederation="CONMEBOL"
        )
        self.team = Team.objects.create(
            name="Ecuador",
            country=self.country,
            group="A"
        )
        self.player = Player.objects.create(
            name="Enner Valencia",
            team=self.team,
            position="FWD",
            jersey_number=13,
            age=34
        )

    def test_player_creation(self):
        self.assertEqual(self.player.name, "Enner Valencia")
        self.assertEqual(self.player.jersey_number, 13)
        self.assertEqual(str(self.player), "Enner Valencia #13 (Ecuador)")

class ViewsTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(
            name="Ecuador",
            code="EC",
            confederation="CONMEBOL"
        )
        self.team = Team.objects.create(
            name="Ecuador",
            country=self.country,
            group="A"
        )
        self.player = Player.objects.create(
            name="Test Player",
            team=self.team,
            position="FWD",
            jersey_number=10
        )

    def test_countries_view(self):
        response = self.client.get(reverse('app_panini:countries'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ecuador')

    def test_players_view(self):
        response = self.client.get(reverse('app_panini:players'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Player')