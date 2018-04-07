from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from .models import Hackathon
from .forms import HackathonForm

def index(request):
    request.session['logged_in'] = True
    request.session['id'] = 1
    events = Hackathon.objects.all()
    if request.session['logged_in']:
        return render(request, 'organizer/index.html', {'events':[{
            'name': event.name,
            'text': event.text
        } for event in events]})

def register(request):
    if request.method == 'POST':
        form = HackathonForm(request.POST)
        if form.is_valid():
            try:
                Hackathon(**form.cleaned_data).save()
            except Exception as e:
                print(e)
                form = HackathonForm()
    else:
        form = HackathonForm()
    return render(request, 'hackatons/register.html', {'form': form})
