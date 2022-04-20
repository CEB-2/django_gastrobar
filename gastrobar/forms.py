from django import forms

# Create your forms here.

#Reservation: name, mail, phone, date, time, count_p

class ReservationForm(forms.Form):
    name=forms.CharField(
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

    phone =forms.CharField(
    max_length=9,
    widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Número de teléfono",
        "type" : "text",
        "pattern" : "[0-9]+"
    }))

    date =forms.DateField(
    widget=forms.DateInput(attrs={
        "class": "form-control",
        "placeholder": "Fecha",
        "type" : "date"
    }))


    time =forms.TimeField(
    widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Hora",
        "type" : "time"
    }))

    count_p =forms.IntegerField(
    widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder": "Número de personas",
        "type" : "number",
        "min" : "0"
        
    }))

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