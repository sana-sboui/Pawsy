from django.shortcuts import render
from django.shortcuts import redirect
#request handler
#return html content to the client
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages 
from django.contrib.auth.models import User
from .forms import RdvForm,ContactForm
from .models import Signup 
from django.contrib.auth  import authenticate,  login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail, EmailMessage 
from django.contrib.auth.decorators import login_required
from .models import  Rdv


def appointment(request):
    if request.method == "POST":
        form = RdvForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Votre formulaire a été soumis avec succès'))
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
            messages.error(request, ('Une erreur est survenue'))
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
    
def klinik(request):
    if request.method == "POST":
        form = RdvForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Votre formulaire a été soumis avec succès'))
            return redirect("klinik.html")
        else:
            Nom = request.POST['Nom']
            Prenom = request.POST['Prénom']
            Email = request.POST['Email']
            Téléphone = request.POST['Téléphone']
            Pet = request.POST['Pet']
            Vet = request.POST['Vet']
            Date = request.POST['Date']
            Service = request.POST['Service']
            Problème = request.POST['Problème']
            messages.error(request, ('Une erreur est survenue'))
            return render(request,"klinik.html", { 'Nom': Nom,
                                                        'Prenom': Prenom,
                                                        'Email': Email,
                                                        'Téléphone': Téléphone,
                                                        'Pet': Pet,
                                                        'Vet': Vet,
                                                        'Date': Date,
                                                        'Service': Service,
                                                        'Problème': Problème,})
    else:
        return render(request ,"klinik.html", {})  

def about(request):
    template=loader.get_template('about.html')
    context={
        'test':'test'
    }
    return HttpResponse(template.render(context,request))

def service(request):
    if request.method == "POST":
        form = RdvForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Votre formulaire a été soumis avec succès'))
            return redirect("klinik.html")
        else:
            Nom = request.POST['Nom']
            Prenom = request.POST['Prenom']
            Email = request.POST['Email']
            Téléphone = request.POST['Téléphone']
            Pet = request.POST['Pet']
            Vet = request.POST['Vet']
            Date = request.POST['Date']
            Service = request.POST['Service']
            Problème = request.POST['Problème']
            messages.error(request, ('Une erreur est survenue'))
            return render(request,"service.html", { 'Nom': Nom,
                                                        'Prenom': Prenom,
                                                        'Email': Email,
                                                        'Téléphone': Téléphone,
                                                        'Pet': Pet,
                                                        'Vet': Vet,
                                                        'Date': Date,
                                                        'Service': Service,
                                                        'Problème': Problème,})
    else:
        return render(request,"service.html", {})
    
def team(request):
    template=loader.get_template('team.html')
    context={
        'test':'test'
    }
    return HttpResponse(template.render(context,request))
    
def feature(request):
    template=loader.get_template('feature.html')
    context={
        'test':'test'
    }
    return HttpResponse(template.render(context,request))

def vet(request):
    template=loader.get_template('vet.html')
    context={
        'test':'test'
    }
    return HttpResponse(template.render(context,request))

def testimonial(request):
    template=loader.get_template('testimonial.html')
    context={
        'test':'test'
    }
    return HttpResponse(template.render(context,request))
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            Nom = request.POST['Nom']
            Prénom = request.POST['Prénom']
            Email = request.POST['Email']
            Sujet = request.POST['Sujet']
            Message = request.POST['Message']

            # send an email
            send_mail(
                Sujet + ' message de ' + Prénom + ' ' + Nom,
                Message,
                Email,  # Use the user-provided email address here
                ['Pawsyvet@gmail.com']
            )
            messages.success(request, 'Votre email a été envoyé avec succès')
            return redirect('klinik.html')
        else:
            Nom = request.POST['Nom']
            Prénom = request.POST['Prénom']
            Email = request.POST['Email']
            Sujet = request.POST['Sujet']
            Message = request.POST['Message']
            messages.error(request, 'Une erreur est survenue')
            return render(request, 'contact.html', {
                'Nom': Nom,
                'Prénom': Prénom,
                'Email': Email,
                'Sujet': Sujet,
                'Message': Message,
            })
    else:
        return render(request, 'contact.html', {})
def adopter(request):
    template=loader.get_template('adopter.html')
    context={
        'test':'test'
    }
    return HttpResponse(template.render(context,request))
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
                messages.error(request, "Vérifiez votre mot de passe")
                return redirect('signup')
                
            # Username should be alphanum
            if Nom_Utilisateur and not Nom_Utilisateur.isalnum() :
                messages.error(request, "Nom d'utilisateur doit contenir seulement des lettres et des chiffres")
                return redirect('signup')
                
            # Create the user
            
            myuser = User.objects.create_user(Nom_Utilisateur, Email, Mot_De_Passe)
            myuser.first_name= Prénom
            myuser.last_name= Nom
            myuser.save()
            return redirect('signup')

        elif 'login' in request.POST:
            # handle login form
            Nom_Utilisateur2 = request.POST.get('Nom_Utilisateur2')
            Mot_De_Passe3 = request.POST.get('Mot_De_Passe3')
            user = authenticate(request, username=Nom_Utilisateur2, password=Mot_De_Passe3)
            if user is not None:
                login(request, user)
                return redirect('klinik/appointments.html')
            else:
                messages.error(request, "Identifiants invalides, veuillez réessayer")
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
    context = {'appointments': appointments, }
    return render(request, 'appointments.html', context)
def logout_view(request):
    logout(request)
    return redirect('signup')
def accept_appointment(request, appointment_id):
    appointment = Rdv.objects.get(id=appointment_id)
    # Perform any necessary acceptance logic here
    
    # Delete the appointment
    appointment.delete()

    # Send an email to the patient
    subject = 'Votre rendez-vous a été accepté'
    message = 'Cher {}, votre rendez-vous du {} a été accepté.'.format(appointment.Nom, appointment.Date)
    from_email = 'Pawsyvet@gmail.com'
    to_email = [appointment.Email]
    email = EmailMessage(subject, message, from_email, to_email)
    email.send()
    return redirect('doctor')
def cancel_appointment(request, appointment_id):
    appointment = Rdv.objects.get(id=appointment_id)
    # Perform any necessary cancellation logic here
    
    # Delete the appointment
    appointment.delete()
    
    # Send an email to the patient
    subject = 'Votre rendez-vous a été annulé'
    message = 'Cher {}, votre rendez-vous du {} a été annulé.'.format(appointment.Nom, appointment.Date)
    from_email = 'Pawsyvet@gmail.com'
    to_email = [appointment.Email]
    email = EmailMessage(subject, message, from_email, to_email)
    email.send()
    return redirect('doctor')
