
from django.core.management.base import BaseCommand  # type: ignore
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):


        # Drop collections directly to avoid PK issues from old data
        from django.db import connection  # type: ignore
        db = connection.cursor().db_conn.client['octofit_db']
        db['activities'].drop()
        db['leaderboard'].drop()
        db['workouts'].drop()
        db['users'].drop()
        db['teams'].drop()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Tony Stark', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Steve Rogers', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Bruce Wayne', email='batman@dc.com', team=dc),
            User.objects.create(name='Clark Kent', email='superman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-11-21')
        Activity.objects.create(user=users[2], type='Cycling', duration=45, date='2025-11-21')
        Activity.objects.create(user=users[3], type='Swimming', duration=60, date='2025-11-21')
        Activity.objects.create(user=users[1], type='Rowing', duration=25, date='2025-11-21')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=195)
        Leaderboard.objects.create(team=dc, points=170)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes', suggested_for='All')
        Workout.objects.create(name='Power Lift', description='Strength training for super strength', suggested_for='All')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
