from django.db import models


class Artist(models.Model):
    GENDER = (("male", "Male"),("female", "Female"))

    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    phone = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)





