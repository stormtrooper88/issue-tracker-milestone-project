from django import forms
from .models import Features

class FeaturePostForm(forms.ModelForm):
    class meta:
        model = Features
        fields = ('name', 'description', 'tag')