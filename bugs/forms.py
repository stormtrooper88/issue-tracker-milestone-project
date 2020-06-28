from django import forms
from .models import Bug

classBugPostForm(forms.ModelForm):
    class meta:
        model = Bug
        fields = ('name', 'description', 'tag')

