from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from .models import Hackathon, HackatonRating
from .forms import HackathonForm


def index(request):
    request.session['logged_in'] = True
    request.session['id'] = 1
    events = Hackathon.objects.all()

    ratings = HackatonRating.objects.all()
    rating_per_event = {}
    for r in ratings:
        print(r.owner, r.rate, type(r.rate))
        print(r.owner.id)
        if r.owner.id not in rating_per_event:
            rating_per_event[r.owner.id] = [-1.0 if r.rate == '-' else 1.0, 0]
        else:
            rs, ns = rating_per_event[r.owner.id]
            # 1.0, 1
            if r.rate == '-':
                rating_per_event[r.owner.id][0] = (rs * ns - 1) / (ns + 1)
            if r.rate == '+':
                rating_per_event[r.owner.id][0] = (rs * ns + 1) / (ns + 1)
        rating_per_event[r.owner.id][1] += 1
    print(rating_per_event)
    return render(request, 'hackathons/index.html', {'events': [{
        'id': event.id,
        'name': event.name,
        'text': event.description,
        'rate': rating_per_event[event.id][0] * 4.0 + 1 if event.id in rating_per_event else 0.0
    } for event in events]})


def register(request):
    if request.method == 'POST':
        form = HackathonForm(request.POST)
        if form.is_valid():
            try:
                Hackathon(**form.cleaned_data).save()
                return redirect('/hackathons')
            except Exception as e:
                print(e)
                form = HackathonForm()
    else:
        form = HackathonForm()
    return render(request, 'hackathons/register.html', {'form': form})


def up(request, id):
    r = HackatonRating.objects.create(owner_id=id, rate='+')
    r.save()
    return index(request)


def down(request, id):
    r = HackatonRating.objects.create(owner_id=id, rate='-')
    r.save()
    return index(request)
