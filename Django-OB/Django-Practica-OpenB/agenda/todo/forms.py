from django.forms import ModelForm, Textarea, TextInput, NumberInput, DateInput
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        exclude = ('date',)
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'date': DateInput(attrs={'class':'form-control', 'disabled':'disabled'}),
            'estimated_end': DateInput(attrs={'class':'form-control', 'type': 'date'}),
            'priority': NumberInput(attrs={'class':'form-control'})
        }
