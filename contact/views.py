""" Contact views mode"""
from django.shortcuts import render, redirect
from django.core.mail import  EmailMessage
from django.urls import  reverse
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["giovicr111@gmail.com"],
                reply_to=[email]
            )

            try:
                #Todo salió bien, redirecionamos
                email.send()
                return redirect(reverse('contact')+ '?ok')
            except:
                #Algo salió mal, redireccionamos
                return redirect(reverse('contact')+ '?fail')

    return render(request, 'contact/contact.html', {'form': contact_form})