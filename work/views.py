from django.shortcuts import render, get_object_or_404

from .models import Work

def allwork(request):
    works = Work.objects
    return render(request, 'work/allwork.html', {'works':works})