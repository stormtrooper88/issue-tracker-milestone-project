from django import forms
from .models import Features

class FeaturePostForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = ('name', 'description', 'tag')