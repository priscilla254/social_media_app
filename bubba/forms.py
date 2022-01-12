from .models import *

from django.forms import ModelForm, Textarea

class BubbasForm(ModelForm):
    class Meta:
        model=Bubbas
        fields=['body']
        widgets = {
            'body': Textarea(attrs={'cols': 50, 'rows': 10}),
        }