from django.conf.urls import url
from drawsaurus.views import api

urlpatterns = [
    url(r'^games/$', api.GameList.as_view()),
    url(r'^games/(?P<pk>[0-9]+)/$', api.GameDetail.as_view()),
    url(r'^games/(?P<game_pk>[0-9]+)/typed_turns$', api.typed_turns_for_game),
    url(r'^games/(?P<game_pk>[0-9]+)/drawing_turns$', api.drawing_turns_for_game),
]