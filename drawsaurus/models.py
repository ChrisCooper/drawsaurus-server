from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)


class Turn(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    turn_number = models.IntegerField()
    author = models.ForeignKey(User)
    game = models.ForeignKey(Game)

    class Meta:
        ordering = ('turn_number',)
        abstract=True


class DrawingTurn(Turn):
    drawing = models.FileField()


class TypedTurn(Turn):
    typed_guess = models.CharField(max_length=100)


class UserProfile(models.Model):
    """
    This model stores the info of a single user, like their money, reputation, etc.
    """
    user = models.OneToOneField(User)
    reputation = models.IntegerField(default=0)