from django.conf.urls import url
from drawsaurus import views

urlpatterns = [
    url(r'^games/$', views.game_list),
    url(r'^games/(?P<pk>[0-9]+)/$', views.game_detail),
    url(r'^games/(?P<game_pk>[0-9]+)/typed_turns$', views.typed_turns_for_game),
    url(r'^games/(?P<game_pk>[0-9]+)/drawing_turns$', views.drawing_turns_for_game),
]