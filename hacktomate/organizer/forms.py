from django import forms
from .models import Organizer

class OrganizerForm(forms.ModelForm):
   class Meta:
       model = Organizer
       fields = '__all__'

   def clean(self):
       cleaned_data = super(OrganizerForm, self).clean()