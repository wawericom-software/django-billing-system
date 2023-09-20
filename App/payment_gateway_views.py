from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single payment_gateway
def payment_gateway_create(request):
    if request.method == 'POST':
        form = payment_gatewayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/home")
        else:
            form = payment_gatewayForm()
    form = payment_gatewayForm(request.POST, request.FILES)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/payment_gateway_create.html", context)

#view for updating a single payment_gateway

def payment_gateway_update(request, pk):
    Payment_gateway = get_object_or_404(payment_gateway, pk=pk)
    form = payment_gatewayForm(request.POST,request.FILES, instance=Payment_gateway)
    if request.method == 'POST':
        form = payment_gatewayForm(request.POST,request.FILES, instance=Payment_gateway)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            form = payment_gatewayForm(request.POST,request.FILES, instance=Payment_gateway)
    context = {
            'form' : form,
            'Payment_gateway' : Payment_gateway,
        }
    return render(request, "Dashboard/payment_gateway_update.html", context)

#view for viewing a single payment_gateways detail

def payment_gateway_detail(request, pk):
    company_payment_gateway = get_object_or_404(payment_gateway, pk=pk)
    context = {
        'company_payment_gateway' : company_payment_gateway
    }
    return render(request, "Dashboard/payment_gateway_detail.html", context)

#view for deleting single payment_gateway

def payment_gateway_delete(request, pk):
    delete_payment_gateway = get_object_or_404(payment_gateway, pk=pk)
    delete_payment_gateway.delete()
    return redirect('/home')

#view for deleting all payment_gateways
def payment_gateways_delete(request):
    delete_payment_gateways = payment_gateway.objects.all()
    delete_payment_gateways.delete()
    return redirect('/home')
    
#view for payment_gateway details

def payment_gateways_detail(request):
    company_payment_gateways = payment_gateway.objects.all()
    context = {
        "company_payment_gateways" : company_payment_gateways
    }
    return render(request, "Dashboard/payment_gateways_detail.html", context)