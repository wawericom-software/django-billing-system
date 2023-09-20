from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single payment_invoice
def payment_invoice_create(request):
    if request.method == 'POST':
        form = payment_invoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home/payment_invoices")
        else:
            form = payment_invoiceForm()
    form = payment_invoiceForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/payment_invoice_create.html", context)

#view for updating a single payment_invoice

def payment_invoice_update(request, pk):
    Payment_invoice = get_object_or_404(payment_invoice, pk=pk)
    form = payment_invoiceForm(request.POST, instance=Payment_invoice)
    if request.method == 'POST':
        form = payment_invoiceForm(request.POST, instance=Payment_invoice)
        if form.is_valid():
            form.save()
            return redirect('/home/payment_invoices')
        else:
            form = payment_invoiceForm(request.POST, instance=Payment_invoice)
    context = {
            'form' : form
        }
    return render(request, "Dashboard/payment_invoice_update.html", context)

#view for viewing a single payment_invoice detail

def payment_invoice_detail(request, pk):
    Payment_invoice = get_object_or_404(payment_invoice, pk=pk)
    context = {
        'payment_invoice' : payment_invoice
    }
    return render(request, "Dashboard/payment_invoice_detail.html", context)

#view for deleting single payment_invoice

def payment_invoice_delete(request, pk):
    payment_invoice_delete = get_object_or_404(payment_invoice, pk=pk)
    payment_invoice_delete.delete()
    return redirect('/home/payment_invoices')

#view for deleting all payment_invoices
def payment_invoices_delete(request):
    delete_invoices = payment_invoice.objects.all()
    delete_invoices.delete()
    return redirect('/home/payment_invoices')
    
#view for payment_invoice details

def payment_invoices_detail(request):
    payment_invoices = payment_invoice.objects.all()
    context = {
        "payment_invoices" : payment_invoices
    }
    return render(request, "Dashboard/payment_invoices_detail.html", context)