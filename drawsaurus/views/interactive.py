from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drawsaurus.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render
from django.http import HttpResponse, Http404
from drawsaurus.models import Game, TypedTurn, DrawingTurn
from drawsaurus.serializers import GameSerializer, TypedTurnSerializer, DrawingTurnSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics

def game_list(request):
    return render(request, 'drawsaurus/game_list.html', {})

def game_detail(request, pk):
    return render(request, 'drawsaurus/game_detail.html', {'game_pk': pk})