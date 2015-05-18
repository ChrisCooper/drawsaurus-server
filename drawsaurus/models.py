from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    next_turn_number = models.IntegerField(default=0)

    class Meta:
        ordering = ('-created',)


class TurnSubmission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    turn_number = models.IntegerField()
    author = models.ForeignKey(User)
    game = models.ForeignKey(Game)

    class Meta:
        ordering = ('turn_number',)
        abstract=True


class DrawingSubmission(TurnSubmission):
    drawing = models.FileField()


class TypedSubmission(TurnSubmission):
    typed_guess = models.CharField(max_length=100)
    

class UserProfile(models.Model):
    """
    This model stores the info of a single user, like their money, reputation, etc.
    """
    user = models.OneToOneField(User)
    reputation = models.IntegerField(default=0)