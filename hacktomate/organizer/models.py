from django.db import models


class Organizer(models.Model):
    name = models.CharField(max_length=80)
    text = models.TextField()
    photo = models.ImageField(upload_to='photos', default='/photos/default.png')
    # list of organized or organizing hackatons
