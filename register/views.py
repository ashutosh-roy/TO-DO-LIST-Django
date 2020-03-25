from django.shortcuts import render
from django.http import HttpResponse
from .models import detail

def index(request):
    #return HttpResponse("Hello World..")
    d = detail.objects.all()
    context = {'d':d}
    return render(request,'voluntaria/register.html',context)
