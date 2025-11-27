from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre", required=True)
    correo = forms.EmailField(label="Correo electrónico")
    asunto = forms.CharField(max_length=200, label="Asunto")
    mensaje = forms.CharField(widget=forms.Textarea, label="Mensaje")
