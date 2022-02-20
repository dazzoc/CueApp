from audioop import reverse
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

MOODS = (
    ('H', 'Happy'),
    ('S', 'Sad'),
    ('C', 'Chillin'),
    ('A', 'Angery'),
)

class Device(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    discription = models.TextField(max_length=250)
    devices = models.ManyToManyField(Device)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'album_id': self.id})

class Listening(models.Model):
    date = models.DateField('Last Listened')
    mood = models.CharField(
        max_length=1,
        choices=MOODS,
        default=MOODS[0][0],
    )
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_mood_display()} on {self.date}"
    # make the most recent feeding at the top to the oldest
    class Meta:
        ordering = ['-date']
