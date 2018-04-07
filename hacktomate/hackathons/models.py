from django.db import models
<<<<<<< Updated upstream
from organizer.models import Organizer
from user.models import Profile
=======
#from hacktomate.organizer.models import Organizer
#from hacktomate.user.models import Profile
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
    owner = models.ForeignKey(Organizer, on_delete=models.DO_NOTHING)
    contestants = models.ManyToManyField(Profile)
=======
#    owner = models.ForeignKey(Organizer)
#    contestants = models.ManyToManyField(Profile)
>>>>>>> Stashed changes

    def __str__(self):
        return self.text
