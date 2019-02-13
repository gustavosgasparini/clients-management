from .models import Client
from django.forms import ModelForm


class ClientForm(ModelForm):

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'age', 'bio', 'photo']