from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    """the home page for HackathonOrganizer"""
    return render(request, 'hackathons/index.html')
