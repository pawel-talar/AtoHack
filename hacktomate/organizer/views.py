from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Organizer
from .forms import OrganizerForm

def index(request):
    request.session['logged_in'] = True
    request.session['id'] = 1
    orgs = Organizer.objects.all()
    print(orgs[0].id)
    if request.session['logged_in']:
        return render(request, 'organizer/index.html', {'orgs':[{
            'name': org.name,
            'text': org.text
        } for org in orgs]})

def register(request):
    if request.method == 'POST':
        form = OrganizerForm(request.POST)
        if form.is_valid():
            try:
                Organizer(**form.cleaned_data).save()
            except Exception as e:
                print(e)
                form = OrganizerForm()
    else:
        form = OrganizerForm()
    return render(request, 'user/register.html', {'form': form})

def profile(request):
    request.session['id'] = 1
    instance = None
    id = 1
    saved = False
    print("lel")
    try:
        instance = get_object_or_404(Organizer, pk=id)
    except Exception as e:
        print(e)
    print("lel 2")
    try:
        print("lel 3")
        form = OrganizerForm(instance=instance)
    except Exception as e:
        print(e)
    return render(request, 'organizer/profile.html', {'form': form, 'saved': saved})
