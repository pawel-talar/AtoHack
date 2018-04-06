from django.contrib import admin

# Register your models here.

from hacktomate.hackathons.models import Tag
from hacktomate.hackathons.models import Hackathon

admin.site.register(Tag)
admin.site.register(Hackathon)