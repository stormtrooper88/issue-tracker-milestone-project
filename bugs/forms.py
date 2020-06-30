from django import forms
from .models import Bug

class BugPostForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('name', 'description', 'tag')

