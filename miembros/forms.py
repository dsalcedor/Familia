from django import forms

class FamiliarForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    edad = forms.IntegerField(label="Edad")
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/05/1998'}))

