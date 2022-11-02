from django.urls import re_path
from django.views.generic import TemplateView

from .views import (
    ArtistListView,
    ArtistRetrieveView,
    AlbumRetrieveView,
)

app_name = 'music'

urlpatterns = [
    re_path(r'^artists/$', ArtistListView.as_view(), name='artist_list'),
    re_path(r'^artists/(?P<pk>\d+)/$', ArtistRetrieveView.as_view(), name='artist_detail'),

    re_path(r'^albums/(?P<pk>\d+)/$', AlbumRetrieveView.as_view(), name='album_detail'),
]
