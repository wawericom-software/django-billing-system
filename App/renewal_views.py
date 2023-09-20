from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from . models import *
from . forms import *
from django.utils import timezone as timezone

def renewal_create():
    pass 

def renewals_detail(request):
    return render(request, 'Dashboard/renewals_detail.html')  

def renewal_detail(request):
    pass 
    
def renewal_status(request):
    pass 

def renewal_update(request):
    pass 

def renewal_delete(request):
    pass 

def renewals_delete(request):
    pass 

