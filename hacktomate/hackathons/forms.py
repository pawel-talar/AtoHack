from django import forms
from .models import Tag
from .models import Hackathon

# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = ['text']
#         labels = {'text': ''}


class HackathonForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        fields = ['text', 'photo', 'tag']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}