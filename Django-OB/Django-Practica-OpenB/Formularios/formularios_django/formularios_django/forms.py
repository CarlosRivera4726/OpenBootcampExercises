from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label="Escribe tu nombre...",
                           max_length=10, required=False)

    url = forms.URLField(label="tu sitio web...", required=False)

    comment = forms.CharField(label="Escribe tu comentario...", required=False)


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre:",
                           max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre...'}))

    email = forms.EmailField(label="Email:",
                             max_length=50,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Ingrese su email...'}))

    message = forms.CharField(label="Mensaje:",
                              widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'rows': '3',
                                                           }))


    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name != 'open':
            raise forms.ValidationError("Tan solo el valor open está permitido")
        else:
            return name