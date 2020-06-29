from django import forms
from .models import Bug

class BugPostForm(forms.ModelForm):
    class meta:
        model = Bug
        fields = ('name', 'description', 'tag')

