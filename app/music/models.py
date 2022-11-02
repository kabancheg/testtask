from django.db import models



class Artist(models.Model):
    name = models.CharField(max_length=128)


class Album(models.Model):
    name = models.CharField(max_length=128)
    year = models.PositiveSmallIntegerField()
    artist = models.ForeignKey(Artist, blank=False, null=False, related_name='albums', on_delete=models.CASCADE)


class Song(models.Model):
    name = models.CharField(max_length=128)
    artist = models.ForeignKey(Artist, blank=False, null=False, related_name='songs', on_delete=models.CASCADE)


class SongOrder(models.Model):
    album = models.ForeignKey(Album, blank=False, null=False, related_name='+', on_delete=models.CASCADE)
    song = models.ForeignKey(Song, blank=False, null=False, related_name='+', on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    
    class Meta:
        unique_together = [['album', 'song']]

