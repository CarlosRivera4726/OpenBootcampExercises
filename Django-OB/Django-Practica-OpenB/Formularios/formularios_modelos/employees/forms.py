from django.forms import ModelForm
from .models import Employee



class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'last_name', 'email'] # ['__all__']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})