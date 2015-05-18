from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drawsaurus.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from drawsaurus.models import Game, TypedTurn, DrawingTurn
from drawsaurus.serializers import GameSerializer, TypedTurnSerializer, DrawingTurnSerializer
from rest_framework.parsers import JSONParser


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


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def game_list(request):
    """
    List all games, or create a new game.
    """
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def game_detail(request, pk):
    """
    Retrieve or delete a game.
    """
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GameSerializer(game)
        return JSONResponse(serializer.data)

    elif request.method == 'DELETE':
        game.delete()
        return HttpResponse(status=204)