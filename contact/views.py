from django.shortcuts import render

from .models import Contact

def allcontact(request):
    contacts = Contact.objects
    return render(request, 'contact/allcontact.html', {'contacts':contacts})