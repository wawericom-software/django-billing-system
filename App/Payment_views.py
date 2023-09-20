from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single Payment
def Payment_create(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home/payments")
        else:
            form = PaymentForm()
    form = PaymentForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/Payment_create.html", context)

#view for updating a single Payment

def Payment_update(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    form = PaymentForm(request.POST, instance=payment)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('/home/payments')
        else:
            form = PaymentForm(request.POST, instance=payment)
    context = {
            'form' : form,
            'payment' : payment
        }
    return render(request, "Dashboard/Payment_update.html", context)

#view for viewing a single Payment detail

def Payment_detail(request, pk):
    company_Payment = get_object_or_404(Payment, pk=pk)
    context = {
        'company_Payment' : company_Payment
    }
    return render(request, "Dashboard/Payment_detail.html", context)

#view for deleting single Payment

def Payment_delete(request, pk):
    Payment_delete = get_object_or_404(Payment, pk=pk)
    Payment_delete.delete()
    return redirect('/home/payments')

#view for deleting all Payments
def Payments_delete(request):
    delete_payments = Payment.objects.all()
    delete_payments.delete()
    return redirect('/home/payments')
    
#view for Payment details

def Payments_detail(request):
    company_Payments = Payment.objects.all()
    context = {
        "company_Payments" : company_Payments
    }
    return render(request, "Dashboard/Payments_detail.html", context)