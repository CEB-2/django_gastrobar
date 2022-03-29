from django import forms

# Create your forms here.

#Comments: user, comment

class CommentsForm(forms.Form):
    user=forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nombre"
        }))

    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Comentario"
        }))


