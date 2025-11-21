from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(team.name, 'Marvel')

    def test_create_user(self):
        team = Team.objects.create(name='DC')
        user = User.objects.create(name='Bruce Wayne', email='bruce@wayne.com', team=team)
        self.assertEqual(user.email, 'bruce@wayne.com')

    def test_create_activity(self):
        team = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Tony Stark', email='tony@stark.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-11-21')
        self.assertEqual(activity.type, 'Running')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='All')
        self.assertEqual(workout.name, 'Pushups')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
