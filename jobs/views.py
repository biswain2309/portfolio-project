from django.shortcuts import render

from .models import Job
from work.models import Work
from achievements.models import Achievements

def home(request):
    works=[]
    jobs = Job.objects
    works = Work.objects.all()[:3]
    achvs = Achievements.objects
    return render(request, 'jobs/home.html', {'jobs':jobs,'works':works,'achvs':achvs})
