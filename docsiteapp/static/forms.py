from django import forms
from .models import Rdv, Signin, Contact
from django.contrib.auth.models import User

"""from .models import Rdv, Signup, Signin
"""
class RdvForm(forms.ModelForm):
    class Meta:
        model = Rdv
        fields = ['Nom', 'Prénom', 'Email', 'Téléphone', 'Pet', 'Vet', 'Date', 'Service', 'Problème']
        widgets = {
            'Vet': forms.Select(attrs={"class": "form-select border-0", "style":"height: 55px;"}),
            'Service': forms.Select(attrs={"class": "form-select border-0", "style": "height: 55px; width: 517px;"})
        }

"""class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup 
        fields = ['Nom', 'Prénom', "Nom_Utilisateur", 'Email', 'Mot_De_Passe', 'Mot_De_Passe2']
"""
class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        required=True,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class SigninForm(forms.ModelForm):
    class Meta:
        model = Signin
        fields = ["Nom_Utilisateur2", 'Mot_De_Passe3']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['Nom', 'Prénom', 'Email', 'Sujet', 'Message']
        widgets = {}    

class MyForm(forms.Form):
    id = forms.IntegerField()

    def clean_id(self):
        id = self.cleaned_data['id']
        if not id:
            raise forms.ValidationError("ID cannot be empty.")
        return id
