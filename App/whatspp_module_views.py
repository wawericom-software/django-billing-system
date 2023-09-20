from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single whatspp_module
def whatspp_module_create(request):
    if request.method == 'POST':
        form = whatspp_moduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home/whatspp_modules")
        else:
            form = whatspp_moduleForm()
    form = whatspp_moduleForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/whatspp_module_create.html", context)

#view for updating a single whatspp_module

def whatspp_module_update(request, pk):
    Whatspp = get_object_or_404(whatspp, pk=pk)
    form = whatspp_moduleForm(request.POST, instance=whatspp)
    if request.method == 'POST':
        form = whatspp_moduleForm(request.POST, instance=Whatspp)
        if form.is_valid():
            form.save()
            return redirect('/home/whatspp_modules')
        else:
            form = whatspp_moduleForm(request.POST, instance=Whatspp)
        context = {
            'form' : form
        }
    return render(request, "Dashboard/whatspp_module_update.html", context)

#view for viewing a single whatspp_modules detail

def whatspp_module_detail(request, pk):
    company_whatspp_module = get_object_or_404(whatspp, pk=pk)
    context = {
        'company_whatspp_module' : company_whatspp_module
    }
    return render(request, "Dashboard/whatspp_module_detail.html", context)

#view for deleting single whatspp_module

def whatspp_module_delete(request, pk):
    whatspp_module_delete = get_object_or_404(whatspp, pk=pk)
    whatspp_module_delete.delete()
    return redirect('/home/whatspp_modules')

#view for deleting all whatspp_modules
def whatspp_modules_delete(request):
    whatspp_delete = whatspp.objects.all()
    whatspp_delete.delete()
    return redirect('/home/whatspp_modules')
    
#view for whatspp_module details

def whatspp_modules_detail(request):
    company_whatspp_modules = whatspp.objects.all()
    context = {
        "company_whatspp_modules" : company_whatspp_modules
    }
    return render(request, "Dashboard/whatspp_modules_detail.html", context)