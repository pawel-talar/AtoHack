from django.db import models
from organizer.models import Organizer
from user.models import Profile

# class Tag:
#     """model representing every available tag"""
#     text = models.CharField(max_length=50)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.text


class Hackathon:
    """a hackathon entry containing it's description and a picture"""
    text = models.TextField()
    photo = models.ImageField(upload_to='photos', default='/photos/default.png')
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Organizer, on_delete=models.DO_NOTHING)
    contestants = models.ManyToManyField(Profile)

    def __str__(self):
        return self.text
