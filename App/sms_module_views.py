from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single sms_module
def sms_module_create(request):
    if request.method == 'POST':
        form = sms_moduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home/sms_modules")
        else:
            form = sms_moduleForm()
    form = sms_moduleForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/sms_module_create.html", context)

#view for updating a single sms_module

def sms_module_update(request, pk):
    Sms = get_object_or_404(sms, pk=pk)
    form = sms_moduleForm(request.POST, instance=Sms)
    if request.method == 'POST':
        form = sms_moduleForm(request.POST, instance=Sms)
        if form.is_valid():
            form.save()
            return redirect('/home/sms_modules')
        else:
            form = sms_moduleForm(request.POST, instance=Sms)
    context = {
            'form' : form,
            'Sms' : Sms
        }
    return render(request, "Dashboard/sms_module_update.html", context)

#view for viewing a single sms_modules detail

def sms_module_detail(request, pk):
    company_sms_module = get_object_or_404(sms, pk=pk)
    context = {
        'company_sms_module' : company_sms_module
    }
    return render(request, "Dashboard/sms_module_detail.html", context)

#view for deleting single sms_module

def sms_module_delete(request, pk):
    sms_module_delete = get_object_or_404(sms, pk=pk)
    sms_module_delete.delete()
    return redirect('/home/sms_modules')

#view for deleting all sms_modules
def sms_modules_delete(request):
    sms_delete = sms.objects.all()
    sms_delete.delete()
    return redirect('/home/sms_modules')
    
#view for sms_module details

def sms_modules_detail(request):
    company_sms_modules = sms.objects.all()
    context = {
        "company_sms_modules" : company_sms_modules
    }
    return render(request, "Dashboard/sms_modules_detail.html", context)