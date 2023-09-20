from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single Address
def Address_create(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home/adress_details")
        else:
            form = AddressForm()
    form = AddressForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/adress_create.html", context)

#view for updating a single Address

def Address_update(request, pk):
    address = get_object_or_404(Address, pk=pk)
    form = AddressForm(request.POST, instance=address)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('/home/adress_details')
        else:
            form = AddressForm(request.POST, instance=address)
    context = {
            'form' : form,
            'address' : address
        }
    return render(request, "Dashboard/adress_update.html", context)

#view for viewing a single Address detail

def Address_detail(request, pk):
    company_Address = get_object_or_404(Address, pk=pk)
    context = {
        'company_Address' : company_Address
    }
    return render(request, "Dashboard/adress_detail.html", context)

#view for deleting single Address

def Address_delete(request, pk):
    if request.method == 'POST':
        Address_delete = get_object_or_404(Address, pk=pk).delete()
        return redirect('/home/adress_details')

#view for deleting all Addresss
def Addresss_delete(request):
    delete_adresses = Address.objects.all()
    delete_adresses.delete()
    return redirect('/home/adress_details')
#view for Address details

def adress_details(request):
    company_Adress = Address.objects.all()
    context = {
        "company_Adress" : company_Adress
    }
    return render(request, "Dashboard/adress_details.html", context)