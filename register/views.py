from django.shortcuts import render
from django.http import HttpResponse

#importing the details wala table from the class 'model'
from .models import *
from .forms import *

def index(request):
    # Stores the value returned by this function
    d = detail.objects.all()
    form= detailForm()
    
    """ Its a dictionary that stores key : value pairs 
    Syntax {'variable___storing___the___date':variable___storing___the___date}"""
    context = {'d':d,'form':form}
    
    # The context is passed to the given HTML Template file 
    return render(request,'voluntaria/register.html',context)
