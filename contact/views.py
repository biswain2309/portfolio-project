from django.shortcuts import render

from .models import Contact

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

from django.core.mail import EmailMessage
from django.conf import settings

from django.http import HttpResponse

import os


# def allcontact(request):
#     contacts = Contact.objects
#     return render(request, 'contact/allcontact.html', {'contacts':contacts})


def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]} {form.cleaned_data["email"]}'
            message = form.cleaned_data['message']
            sender = 'ibiswas.2309@gmail.com'
            recipients = ['indranibiswas23@gmail.com']
            # from_email='ibiswas.2309@gmail.com',
            # to_emails='indranibiswas23@gmail.com',
            # subject='Sending with Twilio SendGrid is Fun',
            # html_content='<strong>and easy to do anywhere, even with Python</strong>')
            try:
                # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                # response = sg.send(message)
                print('*******sender', sender)
                print('*******recipients', recipients)
                print('*******subject', subject)
                print('*******message', message)
                
                send_mail(subject, message, sender, recipients)
                # send_mail('subject', 'message', 'indranibiswas23@gmail.com', ['ibiswas.2309@gmail.com'])
                # return render(request, 'contact/allcontact.html', {'submitted':True})
                # email = EmailMessage(
                #     'Hello', 
                #     'World', 
                #     settings.DEFAULT_FROM_EMAIL, 
                #     to=['indranibiswas23@gmail.com']
                #     )
                # email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            # return HttpResponse('Success!')
            return render(request, 'contact/allcontact.html', {'submitted':True})
    return render(request, 'contact/allcontact.html', {'form':form, 'submitted':False})
