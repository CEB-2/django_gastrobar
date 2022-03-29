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
            "placeholder": "Email"
        }))

    phone =forms.CharField(
    max_length=15,
    widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Número de teléfono"
    }))

    date =forms.DateField(
    widget=forms.DateInput(attrs={
        "class": "form-control",
        "placeholder": "Fecha"
    }))


    time =forms.TimeField(
    widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Hora"
    }))

    count_p =forms.IntegerField(
    widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder": "Número de personas"
    }))
