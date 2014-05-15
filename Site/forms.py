from django import forms

from .models import Site
from django.db.models.base import Model

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site