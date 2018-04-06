from django.db import models


class Profile(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=80)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
