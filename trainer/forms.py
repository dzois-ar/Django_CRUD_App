from django import forms

from .models import Trainer

# create a form tainer
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = [
            'first_name', 'last_name', 'object', 'description', 
            
        ]
