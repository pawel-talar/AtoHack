from django import forms
from .models import Hackathon

# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = ['text']
#         labels = {'text': ''}


class HackathonForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        fields = ['name', 'description', 'owner']
