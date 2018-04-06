from django.urls import path

from . import views

urlpatterns = [
    #empty page
    path('', views.index, name='index'),
    path('hackathons/', views.index, name='index'),

    #page listing all organizators
    #page with hackathons created by specific organization

    #page listing all tags
    #page for adding a new tag

    #page for adding new hackathons (restricted)

]