from rest_framework import serializers
from App.models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
class Payment_gatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = payment_gateway
        fields = '__all__'
        

class Payment_invoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment_invoice
        fields = '__all__'
        
class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = sms
        fields = '__all__'
        
class WhatsppSerializer(serializers.ModelSerializer):
    class Meta:
        model = whatspp
        fields = '__all__'
        
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = email
        fields = '__all__'
        
class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = contacts
        fields = '__all__'
        
class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = campaign
        fields = '__all__'
        
class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'
        
class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = '__all__'
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        
