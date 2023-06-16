from django import forms
#from .models import rdv, test2,contacter
from .models import Rdv,contacter,Signup,Signin



class RdvForm(forms.ModelForm):
    class Meta:
        model = Rdv
        fields = ['Nom','Prénom', 'Email', 'Téléphone','Pet', 'Vet', 'Date','Service', 'Problème']
        widgets = {
            'Vet': forms.Select(attrs={"class": "form-select border-0", "style":"height: 55px;"}),
            'Service': forms.Select(attrs={"class": "form-select border-0", "style": "height: 55px; width: 517px;"})
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = contacter 
        fields = ['Nom','Prénom', 'Email', 'Sujet','Message']
        widgets = {
            
        }
class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup 
        fields = ['Nom','Prénom', "Nom_Utilisateur",'Email','Mot_De_Passe','Mot_De_Passe2']
        widgets = {
            
        }
class SigninForm(forms.ModelForm):
    class Meta:
        model = Signin
        fields = ["Nom_Utilisateur2", 'Mot_De_Passe3']
        widgets = {
            
        }
