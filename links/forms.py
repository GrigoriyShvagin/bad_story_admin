from django import forms

from .models import Links

class AddLinks(forms.ModelForm):
    class Meta:
        model = Links
        fields = ['title', 'link', 'choice']