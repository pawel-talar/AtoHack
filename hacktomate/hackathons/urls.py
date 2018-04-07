from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from hacktomate import settings

from . import views

urlpatterns = [
    #empty page
    path('', views.index, name='index'),

    #page listing all organizators
    #page with hackathons created by specific organization

    #page listing all tags
    #page for adding a new tag

    #page for adding new hackathons (restricted)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
