from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Profile
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
            try:
                Profile(**form.cleaned_data).save()
            except Exception as e:
                print(e)
                form = ProfileForm()
    else:
        form = ProfileForm()
    return render(request, 'user/profile.html', {'form': form})


#@login_required
def profile(request):
    id = 1
    print("lel")
    instance = Profile.objects.get(pk=id)
    print("lel 2")
    saved = False
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=instance)
        if form.is_valid():
            try:
                form.save()
                saved = True
            except Exception as e:
                print(e)
                form = ProfileForm()
    else:
        try:
            print(instance)
            form = ProfileForm(instance=instance)
        except Exception as e:
            print(e)
    return render(request, 'user/profile.html', {'form': form, 'saved': saved})
