from django.db import models


class Profile(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=80)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    cv = models.FileField(null=True, upload_to='documents/')
    location = models.CharField(max_length=30, blank=True)


class Skill(models.Model):
    TECHS = ['c++', 'python', 'javascript', 'postgresql', 'node.js', 'sqlite', 'c#', 'haskell', 'linux']
