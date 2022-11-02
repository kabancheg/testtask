from django.db import transaction
from django.db.models import Q, Value, Subquery, OuterRef, Min, Exists, Sum, F, Count
from django.db.models.functions import Coalesce, JSONObject

from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Artist, Album, Song, SongOrder
from .serializers import ArtistSerializer, AlbumSerializer, AlbumWithArtistSerializer, SongSerializer


class ArtistListView(ListAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class ArtistRetrieveView(APIView):
    
    def get(self, request, pk, *args, **kwargs):
        try:
            artist = Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            return Response({'code': 'does not exist'}, status=status.HTTP_404_NOT_FOUND)

        albums = Album.objects.filter(artist_id=pk).order_by('-year')
        
        data = ArtistSerializer(instance=artist).data
        data['albums'] = AlbumSerializer(instance=albums, many=True).data

        return Response(data, status=status.HTTP_200_OK)


class AlbumRetrieveView(APIView):
    
    def get(self, request, pk, *args, **kwargs):
        try:
            album = Album.objects.select_related('artist').get(pk=pk)
        except Album.DoesNotExist:
            return Response({'code': 'does not exist'}, status=status.HTTP_404_NOT_FOUND)

        songs = Song.objects.filter(artist=album.artist).annotate(
            order=Coalesce(Subquery(
                SongOrder.objects.filter(
                    album_id=pk, song_id=OuterRef('id')).values('order')[:1]
            ), 0),
        ).filter(order__gt=0).order_by('order')

        print(songs.query)

        data = AlbumWithArtistSerializer(instance=album).data
        data['songs'] = SongSerializer(instance=songs, many=True).data

        return Response(data, status=status.HTTP_200_OK)

