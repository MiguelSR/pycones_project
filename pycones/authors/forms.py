from django import forms

from .models import Author
from talks.models import Talk


class AuthorForm(forms.ModelForm):
    talks = forms.ModelMultipleChoiceField(
        queryset=Talk.objects.all(),
        required=False
    )

    class Meta:
        fields = ['name', 'python_level', 'talks']
        model = Author
