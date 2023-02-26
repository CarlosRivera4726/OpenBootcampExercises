from django.forms import ModelForm
from .models import Product
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control', 'placeholder':'Juan José'})

        self.fields['short_description'].widget.attrs.update({'class':'form-control', 'placeholder':'this is a short description'})

        self.fields['description'].widget.attrs.update({'class':'form-control', 'rows':'3'})

        self.fields['stock'].widget.attrs.update({'class':'form-control'})
