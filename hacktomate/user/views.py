from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProfileForm


def index(request):
    request.session['logged_in'] = True
    request.session['id'] = 1
    if request.session['logged_in']:
        return render(request, 'user/index.html')


def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            instance = form.save()
    else:
        form = ProfileForm()
    return render(request, 'user/profile.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ProfileForm()
    return render(request, 'user/profile.html', {'form': form})
