from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.forms import widgets
from drawsaurus.models import Game, TurnSubmission, TypedSubmission, DrawingSubmission


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class GameSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    next_turn_number = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print("Warning: Not allowed to update Games")
        return instance


class TurnSubmissionSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    turn_number = serializers.IntegerField(read_only=True)
    #author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    #game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())

    def update(self, instance, validated_data):
        print("Warning: Not allowed to update TypedSubmissions")
        return instance


class TypedSubmissionSerializer(TurnSubmissionSerializer):
    typed_guess = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return TypedSubmission.objects.create(**validated_data)


class DrawingSubmissionSerializer(TurnSubmissionSerializer):
    drawing = serializers.FileField()

    def create(self, validated_data):
        return DrawingSubmission.objects.create(**validated_data)
