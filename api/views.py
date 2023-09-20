from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from . models import *
from .serializers import *

# Create your views here.
def api_index(request):
    return HttpResponse("hello world")

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class Payment_gatewayListCreateView(generics.ListCreateAPIView):
    queryset = payment_gateway.objects.all()
    serializer_class = Payment_gatewaySerializer
    
class Payment_invoiceListCreateView(generics.ListCreateAPIView):
    queryset = payment_invoice.objects.all()
    serializer_class = Payment_invoiceSerializer
    
class WhatsppListCreateView(generics.ListCreateAPIView):
    queryset = whatspp.objects.all()
    serializer_class = WhatsppSerializer
    
class SmsListCreateView(generics.ListCreateAPIView):
    queryset = sms.objects.all()
    serializer_class = SmsSerializer
    
class EmailListCreateView(generics.ListCreateAPIView):
    queryset = email.objects.all()
    serializer_class = EmailSerializer
    
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = contacts.objects.all()
    serializer_class = ContactsSerializer
    
class campaignListCreateView(generics.ListCreateAPIView):
    queryset = campaign.objects.all()
    serializer_class = CampaignSerializer
        
class PackagesListCreateView(generics.ListCreateAPIView):
    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer
        
class ProductItemListCreateView(generics.ListCreateAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
        
class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
        
        