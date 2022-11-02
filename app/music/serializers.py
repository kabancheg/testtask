from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Artist, Album, Song


class AlbumSerializer(ModelSerializer):

    class Meta:
        model = Album
        fields = ('id', 'name', 'year')
        read_only_fields = ('id', 'name', 'year')


class ArtistSerializer(ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id', 'name',)
        read_only_fields = ('id', 'name',)


class SongSerializer(ModelSerializer):
    order = SerializerMethodField()

    class Meta:
        model = Song
        fields = ('id', 'name', 'order')
        read_only_fields = ('id', 'name', 'order')

    def get_order(self, obj):
        return getattr(obj, 'order', 0)


class AlbumWithArtistSerializer(ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'name', 'year', 'artist')
        read_only_fields = ('id', 'name', 'year', 'artist')

