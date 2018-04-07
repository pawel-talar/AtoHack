from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

import pdftotext

from .models import Profile, Skill
from .forms import ProfileForm


def index(request):
    request.session['logged_in'] = True
    request.session['id'] = 1
    users = Profile.objects.all()
    if request.session['logged_in']:
        return render(request, 'user/index.html', {'users':  users})


def register(request):
    request.session['id'] = 1
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


def handle_skills(filepath, user_id):
    pdf = pdftotext.PDF(filepath.open())
    text = ''.join(pdf).lower()
    print(text)
    for tech in Skill.TECHS_:
        if tech in text:
            skill = Skill.objects.create(user_id=user_id, skill=tech)
            skill.save()


def profile(request):
    request.session['id'] = 1
    instance = None
    id = 1
    print("lel")
    try:
        instance = get_object_or_404(Profile, pk=id)
    except Exception as e:
        print(e)
    print("lel 2")
    saved = False
    if request.method == 'POST':
        print("lel :D :D")
        form = ProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            print('valid')
            try:
                file_path = request.FILES['cv']
                print(request.FILES['cv'])
                profile = form.save()
                handle_skills(file_path, request.session['id'])
                saved = True
            except Exception as e:
                print(e)
                form = ProfileForm(instance=instance)
        else:
            print('invalid')
            messages.error(request, "Error")
    else:
        try:
            print("lel 3")
            form = ProfileForm(instance=instance)
        except Exception as e:
            print(e)
    return render(request, 'user/profile.html', {'form': form, 'saved': saved})
