from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'shirt_size', 'location']

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
