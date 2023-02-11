from django import forms
from .models import createNews

class NewsForm(forms.ModelForm):
    class Meta:
        model = createNews
        fields = ['title', 'newsDetails', 'coverImage']
