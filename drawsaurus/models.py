from django.db import models
from django.contrib.auth.models import User


class TurnSubmission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    turn_number = models.IntegerField()
    author = models.ForeignKey(User)
    game = models.ForeignKey('Game')

    DRAWING = 'DR'
    TYPED_GUESS = 'TY'
    TURN_TYPE_CHOICES = (
        (DRAWING, 'Drawing'),
        (TYPED_GUESS, 'Typed Guess'),
    )
    turn_type = models.CharField(max_length=2,
                                 choices=TURN_TYPE_CHOICES)

    typed_guess = models.CharField(max_length=100)
    drawing = models.FileField()

    class Meta:
        ordering = ('turn_number',)


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)


class UserProfile(models.Model):
    """
    This model stores the info of a single user, like their money, reputation, etc.
    """
    user = models.OneToOneField(User)
    reputation = models.IntegerField(default=0)