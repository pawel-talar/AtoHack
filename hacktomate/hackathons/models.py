from django.db import models

class Tag:
    text = models.CharField(max_length=50)

class Hackaton:
    desc = models.TextField()
    photo = models.ImageField(upload_to='photos', default='/photos/default.png')
    tag = models.ManyToManyField(Tag)
    date_added = models.DateTimeField(auto_now_add=True)
   # owner = models.ForeignKey(Organizer)
   # contestants = models.ManyToManyField(Profile)

# Create your models here.
