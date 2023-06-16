from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Rdv(models.Model):
    Vet_Choices = [
        ('', 'choisissez un vétérinaire'),
        ("1", "inesarfa"),
        ("2", "sofieneelali"),
        ("3", "mariemayed"),
        ("4", "Rachedhajar"),
        ("5", "Ferdawshanbouli"),
        ("6", "Ranimeelhkir"),
        ("7", "saberbouhada"),
        ("8", " amenibilhaj"),
    ]
    Service_Choices = [
        ('', 'Choisissez un service'),
        ('1', 'Consultation'),
        ('2', 'Vaccinations'),
        ('3', 'Micropuçage'),
        ('4', 'Pension'),
        ('5', 'Soins Dentaires'),
    ]
    Nom = models.CharField(max_length=30)
    Prénom = models.CharField(max_length=30)
    Email = models.EmailField(unique=True)
    Téléphone = models.CharField(max_length=30)
    Pet = models.CharField(max_length=30)
    Vet = models.CharField(max_length=1, choices=Vet_Choices)
    Date = models.DateTimeField()
    Service = models.CharField(max_length=1, choices=Service_Choices)
    Problème = models.CharField(max_length=240, blank=True, null=True)
    vet = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rdv')

    def __str__(self):
        return self.Nom + " " + self.Prénom
   
"""class Signup(models.Model):
    Nom = models.CharField(max_length=30,default="")
    Prénom=models.CharField(max_length=30,default="")
    Nom_Utilisateur=models.CharField(max_length=30,default="",unique = True)
    Email = models.EmailField(unique = True)
    Mot_De_Passe=models.CharField(label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}), 
        required=True,)
    Mot_De_Passe2=models.CharField(label="Confirm Password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        required=True,)

    def __str__(self):
        return self.Nom + " "+ self.Prénom"""

class Signin(models.Model):
    Nom_Utilisateur2=models.CharField(max_length=30,default="",unique = True)
    Mot_De_Passe3=models.CharField(max_length=30,default="")
    
    def __str__(self):
        return self.Nom_Utilisateur2
    
class Contact(models.Model):
    Nom = models.CharField(max_length=30)
    Prénom = models.CharField(max_length=30)
    Email = models.EmailField(unique = True)
    Sujet = models.CharField(max_length=30)
    Message = models.CharField(max_length=250)

    def __str__(self):
        return self.Nom + " " + self.Prénom