from django.test import TestCase
from .models import User, Team

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Marvel")
        user = User.objects.create(name="Spider-Man", email="spiderman@marvel.com", team=team)
        self.assertEqual(user.name, "Spider-Man")
