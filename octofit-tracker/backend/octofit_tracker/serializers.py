from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity', 'duration']

class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'duration']
