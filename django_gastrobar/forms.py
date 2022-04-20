from django import forms

class ContactoForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nombre"
        }))

    mail = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Email",
            "type" : "email"
        }))

    asunto = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Asunto"
        }))

    mensaje = forms.CharField(
        widget = forms.Textarea(attrs={
            "class" : "form-control",
            "placeholder" : "Mensaje"
        }))