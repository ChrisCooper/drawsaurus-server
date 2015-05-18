from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.forms import widgets
from drawsaurus.models import Game, Turn, TypedTurn, DrawingTurn


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('pk', 'created', 'next_turn_number')


class TurnSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    turn_number = serializers.IntegerField(read_only=True)
    #author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    #game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())

    def create(self, validated_data):
        print("Error: can't create abstract model 'Turn'")
        return None

    def update(self, instance, validated_data):
        print("Warning: Not allowed to update TypedTurns")
        return instance


class TypedTurnSerializer(TurnSerializer):
    typed_guess = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return TypedTurn.objects.create(**validated_data)


class DrawingTurnSerializer(TurnSerializer):
    drawing = serializers.FileField()

    def create(self, validated_data):
        return DrawingTurn.objects.create(**validated_data)

