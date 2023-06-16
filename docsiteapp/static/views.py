from django.shortcuts import render,redirect

#request handler
#return html content to the client

from django.http import HttpResponse
from django.template import loader
from .models import Rdv, Signin
from .forms import RdvForm, SignUpForm, ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required



def say_hello(request):
    template = loader.get_template('klinik.html')
    context={
        'test':'test'
    }
    return HttpResponse(template.render(context,request))
def team(request):
    return render(request,"team.html")
def about(request):
    return render(request,"about.html")
def appointment(request):
    if request.method == "POST":
        form = RdvForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Votre rendez-vous a été enregistré avec succès !'))
            return redirect("klinik.html")
        else:
            Nom = request.POST['Nom']
            Prénom = request.POST['Prénom']
            Email = request.POST['Email']
            Téléphone = request.POST['Téléphone']
            Pet = request.POST['Pet']
            Vet = request.POST['Vet']
            Date = request.POST['Date']
            Service = request.POST['Service']
            Problème = request.POST['Problème']
            messages.error(request, ('Veuillez remplir champs correctement.'))
            return render(request,"appointment.html", { 'Nom': Nom,
                                                        'Prénom': Prénom,
                                                        'Email': Email,
                                                        'Téléphone': Téléphone,
                                                        'Pet': Pet,
                                                        'Vet': Vet,
                                                        'Date': Date,
                                                        'Service': Service,
                                                        'Problème': Problème,})
    else:
        return render(request,"appointment.html", {})

def contact(request):
    if request.method == "POST":
        Nom = request.POST['Nom']
        Prénom = request.POST['Prénom']
        Email = request.POST['Email']
        Sujet = request.POST['Sujet']
        Message = request.POST['Message']

        # send an email 
        send_mail(
            Sujet + 'message de ' + Prénom + Nom,
            Message,
            Email,
            ['sbouisana1234@gmail.com']
        )
        return render(request,"contact.html", {     'Nom': Nom,
                                                    'Prénom': Prénom,
                                                    'Email': Email,
                                                    'Sujet': Sujet,
                                                    'Message': Message,})
    else:    
        return render(request,"contact.html")
def klinik(request):
    return render(request,"klinik.html")
def service(request):
    return render(request,"service.html")
def testimonial(request):
    return render(request,"testimonial.html")
def feature(request):
    return render(request,"feature.html")
def vet(request):
    return render(request, "vet.html")
def adopter(request):
    return render(request, "adopter.html")
def signup_login(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            # handle sign up form
            Nom= request.POST.get('Nom')
            Prénom = request.POST.get('Prénom')
            Nom_Utilisateur = request.POST.get('Nom_Utilisateur')
            Email = request.POST.get('Email')
            Mot_De_Passe = request.POST.get('Mot_De_Passe')
            Mot_De_Passe2=request.POST.get('Mot_De_Passe2')
            
            # check for errorneous input
            # Passwords should match 
            if (Mot_De_Passe != Mot_De_Passe2):
                messages.error(request, "Passwords do not match")
                return redirect('signup')
                
            # Username should be alphanum
            if Nom_Utilisateur and not Nom_Utilisateur.isalnum() :
                messages.error(request, "Username should only contain letters and numbers")
                return redirect('signup')
                
            # Create the user
            
            myuser = User.objects.create_user(Nom_Utilisateur, Email, Mot_De_Passe)
            myuser.first_name= Prénom
            myuser.last_name= Nom
            myuser.save()
            messages.success(request, "Your account has been successfully created")
            return redirect('klinik')

        elif 'login' in request.POST:
            # handle login form
            Nom_Utilisateur2 = request.POST.get('Nom_Utilisateur2')
            Mot_De_Passe3 = request.POST.get('Mot_De_Passe3')
            user = authenticate(request, username=Nom_Utilisateur2, password=Mot_De_Passe3)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect('klinik/appointments.html')
            else:
                messages.error(request, "Invalid credentials, please try again")
                return redirect('signup')
    else:
        return render(request, 'signup.html')
    
@login_required
def appointment_list(request):
    username = request.user.username
    if username=="inesarfa":
        appointments = Rdv.objects.filter(Vet='1')
    elif username=="sofieneelali":
        appointments = Rdv.objects.filter(Vet='2')
    elif username=="mariemayed":
        appointments = Rdv.objects.filter(Vet='3')
    elif username=="rachedhajar":
        appointments = Rdv.objects.filter(Vet='4')
    elif username=="ferdawshanbouli":
        appointments = Rdv.objects.filter(Vet='5')
    elif username=="ranimeelhkir":
        appointments = Rdv.objects.filter(Vet='6')   
    elif username=="saberbouhada":
        appointments = Rdv.objects.filter(Vet='7') 
    elif username=="amenibilhaj ":
        appointments = Rdv.objects.filter(Vet='8') 
    context = {'appointments': appointments }
    return render(request, 'appointments.html', context)