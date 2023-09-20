from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single order
def order_create(request):
    form = OrderForm(request.POST)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home/orders")
        else:
            form = OrderForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/order_create.html", context)

#view for updating a single order

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST, instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/home/orders')
        else:
            form = OrderForm(request.POST, instance=order)
    context = {
            'form' : form,
            'order' : order
        }
    return render(request, "Dashboard/order_update.html", context)

#view for viewing a single orders detail

def order_detail(request, pk):
    company_order = get_object_or_404(Order, pk=pk)
    context = {
        'company_order' : company_order
    }
    return render(request, "Dashboard/order_detail.html", context)

#view for deleting single order

def order_delete(request, pk):
    order_delete = get_object_or_404(Order, pk=pk)
    order_delete.delete()
    return redirect('/home/orders')

#view for deleting all orders
def orders_delete(request):
    delete_orders = Order.objects.all()
    delete_orders.delete()
    return redirect('/home/orders')
    
#view for order details

def orders_detail(request):
    company_orders = Order.objects.all()
    context = {
        "company_orders" : company_orders
    }
    return render(request, "Dashboard/orders_detail.html", context)