from django.forms import ModelForm, Textarea, TextInput, EmailInput, DateInput
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date',)
        widgets = {
            'first_name': TextInput(attrs={'class':'form-control'}),
            'last_name': TextInput(attrs={'class':'form-control'}),
            'phone': TextInput(attrs={'class':'form-control'}),
            'mobile': TextInput(attrs={'class':'form-control'}),
            'email': EmailInput(attrs={'class':'form-control'}),
            'company': TextInput(attrs={'class':'form-control'}),
            'date': DateInput(attrs={'class':'form-control'}),
            'notes': Textarea(attrs={'class':'form-control', 'rows':'3'}),
        }