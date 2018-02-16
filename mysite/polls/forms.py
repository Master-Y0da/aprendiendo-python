from django import forms


class CommentForm(forms.Form):
    email = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email', 'name': 'email'}))
    password = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Contraseña', 'name': 'password'}))
