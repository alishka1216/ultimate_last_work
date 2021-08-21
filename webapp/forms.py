from django import forms
from webapp.models import Announcement


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'description', 'avatar','category', 'moderate', 'price',]