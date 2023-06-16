from django.db import models
from django.contrib.auth.models import User


class contacter(models.Model):
    Nom = models.CharField(max_length=40,default='')  # length must be precise to not take space
    Prénom = models.CharField(max_length=40, default='')
    Email = models.EmailField(max_length=100)
    Sujet=models.CharField(max_length=40,default='')
    Message=models.CharField(max_length=400,default='')
    def __str__(self):
         return self.Nom+ " " + self.Prénom # to name the database 

class Signup(models.Model):
    Nom = models.CharField(max_length=30,default="")
    Prénom=models.CharField(max_length=30,default="")
    Nom_Utilisateur=models.CharField(max_length=30,default="",unique = True)
    Email = models.EmailField(unique = True)
    Mot_De_Passe=models.CharField(max_length=30,default="")
    Mot_De_Passe2=models.CharField(max_length=30,default="")
    def __str__(self):
        return self.Nom + " "+ self.Prénom
class Signin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='signin',default=1)
    Nom_Utilisateur2=models.CharField(max_length=30,default="",unique = True)
    Mot_De_Passe3=models.CharField(max_length=30,default="")

    def __str__(self):
        return self.Nom_Utilisateur2
    




class Rdv(models.Model):
    Vet_Choices = [
        ("","choisissez votre vétérinaire"),
        ("1", "inesarfa"),
        ("2", "sofieneelali"),
        ("3", "mariemayed"),
        ("4", "Rachedhajar"),
        ("5", "Ferdawshanbouli"),
        ("6", "Ranimeelhkir"),
        ("7", "saberbouhada"),
        ("8", "amenibilhaj"),
    ]
    Service_Choices = [
        ("","choisissez votre service"),
        ("1", "Consultation"),
        ("2", "Vaccinations"),
        ("3", "Micropuçage"),
        ("4", "Pension"),
        ("5", "Soins Dentaires"),
        ("6", "Toilettage"),
      
    ]
    Nom = models.CharField(max_length=30,default="")
    Prénom=models.CharField(max_length=30,default="")
    Email = models.EmailField(unique = True)
    Téléphone = models.IntegerField()
    Pet = models.CharField(max_length=30,default="")
    Vet = models.CharField(max_length=1, choices=Vet_Choices,blank=True , null=True)
    Date = models.DateTimeField()
    Service = models.CharField(max_length=1, choices=Service_Choices,blank=True , null=True)
    Problème = models.CharField(max_length=240, blank=True, null=True)
    def __str__(self):
        return self.Nom + " "+ self.Prénom
