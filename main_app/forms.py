from django.forms import ModelForm
from .models import Listening

class ListeningForm(ModelForm):
    class Meta:
        model = Listening
        fields = ('date', 'mood')