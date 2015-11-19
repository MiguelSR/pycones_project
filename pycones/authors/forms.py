from django import forms

from .models import Author
from talks.models import Talk


class AuthorForm(forms.ModelForm):
    talks = forms.ModelMultipleChoiceField(
        Talk.objects.all(),
        required=False
    )

    class Meta:
        fields = ['name', 'python_level', 'talks']
        model = Author

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['talks'] = Talk.objects.filter(authors=self.instance)

    def save(self, *args, **kwargs):
        instance = super(AuthorForm, self).save(*args, **kwargs)

        if instance.pk:
            for talk in instance.talks.all():
                if talk not in self.cleaned_data['talks']:
                    instance.talks.remove(talk)

            for talk in self.cleaned_data['talks']:                  
                if talk not in instance.talks.all():                   
                    instance.talks.add(talk)

        return instance
