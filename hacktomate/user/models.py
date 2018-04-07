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
    TECHS_ = ('c++', 'python', 'javascript', 'postgresql', 'node.js', 'sqlite', 'c#', 'haskell', 'linux')
    TECHS = tuple(zip(TECHS_, TECHS_))

    user = models.ForeignKey(
        Profile,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    skill = models.CharField(max_length=20, choices=TECHS)
