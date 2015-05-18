from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drawsaurus.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from drawsaurus.models import Game, TypedTurn, DrawingTurn
from drawsaurus.serializers import GameSerializer, TypedTurnSerializer, DrawingTurnSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def interactive(request):
    return render(request, 'default.html', {})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET', 'POST'])
def game_list(request):
    """
    List all games, or create a new game.
    """
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def game_detail(request, pk):
    """
    Retrieve or delete a game.
    """
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GameSerializer(game)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        game.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def typed_turns_for_game(request, game_pk):
    """
    Returns the ordered list of all turns so far in a game.
    """
    if request.method == 'GET':
        try:
            game = Game.objects.get(pk=game_pk)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        typed_turns = TypedTurn.objects.filter(game=game)
        typed_serializer = TypedTurnSerializer(typed_turns, many=True)
        return Response(typed_serializer.data)


@api_view(['GET'])
def drawing_turns_for_game(request, game_pk):
    """
    Returns the ordered list of all turns so far in a game.
    """
    if request.method == 'GET':
        try:
            game = Game.objects.get(pk=game_pk)
        except Game.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        drawing_turns = DrawingTurn.objects.filter(game=game)
        drawing_serializer = DrawingTurnSerializer(drawing_turns, many=True)
        return Response(drawing_serializer.data)