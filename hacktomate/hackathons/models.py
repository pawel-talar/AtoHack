from django.db import models
from organizer.models import Organizer
from user.models import Profile


class Hackathon(models.Model):
    """a hackathon entry containing it's description and a picture"""
    name = models.CharField(max_length=30)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    rate = models.FloatField(default=0.0)
    owner = models.ForeignKey(Organizer, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.name


class HackatonRating(models.Model):
    RATINGS = (('-', 'down'), ('+', 'up'))
    rate = models.CharField(max_length=1, choices=RATINGS)
    owner = models.ForeignKey(Hackathon, on_delete=models.DO_NOTHING)
