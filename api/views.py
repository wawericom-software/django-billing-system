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

class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class  = ClientSerializer
    
class Payment_gatewayListCreateView(generics.ListCreateAPIView):
    queryset = payment_gateway.objects.all()
    serializer_class = Payment_gatewaySerializer

class Payment_gatewayRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = payment_gateway.objects.all()
    serializer_class = Payment_gatewaySerializer
    
class Payment_invoiceListCreateView(generics.ListCreateAPIView):
    queryset = payment_invoice.objects.all()
    serializer_class = Payment_invoiceSerializer

class Payment_invoiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = payment_invoice.objects.all()
    serializer_class = Payment_invoiceSerializer
    
class WhatsppListCreateView(generics.ListCreateAPIView):
    queryset = whatspp.objects.all()
    serializer_class = WhatsppSerializer
    
class WhatsppRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = whatspp.objects.all()
    serializer_class = WhatsppSerializer

class SmsListCreateView(generics.ListCreateAPIView):
    queryset = sms.objects.all()
    serializer_class = SmsSerializer

class SmsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = sms.objects.all()
    serializer_class = SmsSerializer
    
class EmailListCreateView(generics.ListCreateAPIView):
    queryset = email.objects.all()
    serializer_class = EmailSerializer

class EmailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = email.objects.all()
    serializer_class = EmailSerializer
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = contacts.objects.all()
    serializer_class = ContactsSerializer

class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset  = contacts.objects.all()
    serializer_class = ContactsSerializer
    
class campaignListCreateView(generics.ListCreateAPIView):
    queryset = campaign.objects.all()
    serializer_class = CampaignSerializer

class campaignRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = campaign.objects.all()
    serializer_class = CampaignSerializer
        
class PackagesListCreateView(generics.ListCreateAPIView):
    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer

class PackagesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer
        
class ProductItemListCreateView(generics.ListCreateAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer

class ProductItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
        
class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
        

class profile_viewsListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = profile_viewsSerializer

class profile_viewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = profile_viewsSerializer