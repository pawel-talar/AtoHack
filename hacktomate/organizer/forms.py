from django import forms
from .models import Organizer

class OrganizerForm(forms.Form):
   class Meta:
       model = Organizer
       fields = ['name', 'text', 'photo']

   def clean(self):
       cleaned_data = super(ProfileForm, self).clean()