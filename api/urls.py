from django.urls import path
from . import views
from . views import ClientListCreateView, ClientRetrieveUpdateDestroyView, Payment_gatewayListCreateView, Payment_gatewayRetrieveUpdateDestroyView
from . views import Payment_invoiceListCreateView, Payment_invoiceRetrieveUpdateDestroyView, WhatsppListCreateView, WhatsppRetrieveUpdateDestroyView
from . views import SmsListCreateView, SmsRetrieveUpdateDestroyView, EmailListCreateView, EmailRetrieveUpdateDestroyView
from . views import ContactListCreateView, ContactRetrieveUpdateDestroyView, campaignListCreateView, campaignRetrieveUpdateDestroyView
from . views import PackagesListCreateView, PackagesRetrieveUpdateDestroyView, ProductItemListCreateView, ProductItemRetrieveUpdateDestroyView
from . views import OrderItemListCreateView, OrderItemRetrieveUpdateDestroyView, PaymentListCreateView, PaymentRetrieveUpdateDestroyView

urlpatterns = [
    path('', views.api_index, name='api_index'),
    
    # urls for client
    path('clients/', ClientListCreateView.as_view(), name='client_list_create'),
    path('client/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name=' ClientRetrieveUpdateDestroyView'),

    # urls for payment gateway
    path('payment_gateways/', Payment_gatewayListCreateView.as_view(), name = 'payment_gateway_list_create'),
    path('payment_gateway/<int:pk>/', Payment_gatewayRetrieveUpdateDestroyView.as_view(), name='Payment_gatewayRetrieveUpdateDestroyView'),

    # urls for payment invoices
    path('payment_invoices/', Payment_invoiceListCreateView.as_view(), name='payment_invoice_list_create'),
    path('payment_invoice/<int:pk>/', Payment_invoiceRetrieveUpdateDestroyView.as_view(), name='Payment_invoiceRetrieveUpdateDestroyView'),

    # urls for whatspp
    path('whatspps/', WhatsppListCreateView.as_view(), name='whatspp_list_create'),
    path('whatspp/<int:pk>/', WhatsppRetrieveUpdateDestroyView.as_view(), name='WhatsppRetrieveUpdateDestroyView'),

    # Urls for sms
    path('smss/', SmsListCreateView.as_view(), name='sms_list_create'),
    path('sms/<int:pk>/', SmsRetrieveUpdateDestroyView.as_view(), name='SmsRetrieveUpdateDestroyView'),

    # Urls for email
    path('emails/', EmailListCreateView.as_view(), name='email_list_create'),
    path('email/<int:pk>/', EmailRetrieveUpdateDestroyView.as_view(), name='EmailRetrieveUpdateDestroyView'),

    # Urls for contacts
    path('contacts/', ContactListCreateView.as_view(), name='contacts_list_create'),
    path('contact/<int:pk>/', ContactRetrieveUpdateDestroyView.as_view(), name='ContactRetrieveUpdateDestroyView'),

    #   Urls for camphains
    path('camphaigns/', campaignListCreateView.as_view(), name='camphain_list_create'),
    path('camphain/<int:pk>/', campaignRetrieveUpdateDestroyView.as_view(), name='campaignRetrieveUpdateDestroyView'),

    # Urls for packages
    path('packages/', PackagesListCreateView.as_view(), name='packages_list_create'),
    path('package/<int:pk>/',  PackagesRetrieveUpdateDestroyView.as_view(), name=' PackagesRetrieveUpdateDestroyView'),

    # Urls for product items
    path('productitems/', ProductItemListCreateView.as_view(), name='product_item_list_create'),
    path('productitem/<int:pk>/', ProductItemRetrieveUpdateDestroyView.as_view(), name='ProductItemRetrieveUpdateDestroyView'),

    # Urls for orders
    path('orders/', OrderItemListCreateView.as_view(), name='order_item_list_create_view'),
    path('order/<int:pk>/',OrderItemRetrieveUpdateDestroyView.as_view(), name='OrderItemRetrieveUpdateDestroyView'),

    # Urls for payments
    path('payments/', PaymentListCreateView.as_view(), name='payment_list_create'),
    path('payment/<int:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='PaymentRetrieveUpdateDestroyView'),
]