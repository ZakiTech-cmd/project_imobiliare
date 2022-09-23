from django.forms import ModelForm
from .models import Announce

class AnnounceForm(ModelForm):
    class Meta:
        model = Announce
        fields = '__all__'