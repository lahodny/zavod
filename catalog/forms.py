from django.forms import ModelForm

from catalog.models import Race


class RaceModelForm(ModelForm):
    class Meta:
        model = Race
        fields = ['name', 'date', 'athlete', 'discipline']
