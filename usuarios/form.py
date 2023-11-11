from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        max_length=100,
        required=True,
        label='Nome de Login'
    )
    senha = forms.CharField(
        max_length=100,
        required=True,
        label='Senha',
        widget=forms.PasswordInput()
    )