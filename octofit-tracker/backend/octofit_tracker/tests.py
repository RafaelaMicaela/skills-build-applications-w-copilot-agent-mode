from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.team = Team.objects.create(name='Test Team')
        self.team.members.add(self.user)
        self.activity = Activity.objects.create(user=self.user, activity='Running', duration=30)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)
        self.workout = Workout.objects.create(name='Morning Run', description='Quick run', duration=30)

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity, 'Running')

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 100)

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Morning Run')
