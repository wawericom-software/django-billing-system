from django.shortcuts import render, redirect
from django.db.models import Sum, Avg
from django.http import HttpResponse
from . models import *
from . forms import *
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    total_clients = Client.objects.count()
    total_packages = Packages.objects.count()
    total_products = ProductItem.objects.count()
    total_campaigns = campaign.objects.count()
    total_contacts = contacts.objects.count()
    total_invoices = payment_invoice.objects.count()
    total_orders = Order.objects.count()
    Payment_gateway = payment_gateway.objects.count()
    total_income = Payment.objects.aggregate(income=Sum('amount'))['income']
    context = {
        'total_clients' : total_clients,
        'total_packages' : total_packages,
        'total_products' : total_products,
        'total_campaigns' : total_campaigns,
        'total_contacts' : total_contacts,
        'total_invoices' : total_invoices,
        'total_orders' : total_orders,
        'Payment_gateway' : Payment_gateway,
        'total_income' : total_income
    }
    return render(request, "Dashboard/index.html", context)

# payment views
def payments(request):
    return render(request, "Dashboard/payments.html")

# daily report views
def dailyReports(request):
    date = datetime.now()
    context = {
        'date' : date
    }
    return render(request, "Dashboard/dailyReports.html", context)

#  Monthly Report views
def monthlyReports(request):
    date = datetime.now()
    context = {
        'date' : date
    }
    return render(request, "Dashboard/monthlyReports.html", context)

# Yearly Reports views
def yearlyReports(request):
    date = datetime.now()
    context = {
        'date' : date
    }
    return render(request, "Dashboard/yearlyReports.html", context)

# settings module
def settings(request):
    return render(request, "Dashboard/settings.html")

# profile
def profile(request):
    return render(request, "Dashboard/profile.html")


# login function
def login(request):
    return

# logout function
def logout(request):
    pass