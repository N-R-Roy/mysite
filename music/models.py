
from django.db import models
from django.urls import reverse


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=250)
    album_logo = models.FileField()

    def __str__(self):
        return self.album_title + " - " + self.artist

    # When new instance create, that time this method is called
    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'id': self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title

    # When new instance create, that time this method is called
    def get_absolute_url(self):
        obj = Song.objects.get(id=self.pk)
        return reverse('music:detail', kwargs={'pk': obj.album.id})


class Test(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    Login_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    # When new instance create, that time this method is called
    # def get_absolute_url(self):
    #     return reverse('music:index')

