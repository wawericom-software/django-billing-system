from django.urls import path
from . import views
from . views import ClientListCreateView, ContactRetrieveUpdateDestroyView, Payment_gatewayListCreateView, Payment_gatewayRetrieveUpdateDestroyView
from . views import Payment_invoiceListCreateView, Payment_invoiceRetrieveUpdateDestroyView, WhatsppListCreateView, WhatsppRetrieveUpdateDestroyView
from . views import SmsListCreateView, SmsRetrieveUpdateDestroyView, EmailListCreateView, EmailRetrieveUpdateDestroyView
from . views import ContactListCreateView, ContactRetrieveUpdateDestroyView, campaignListCreateView, campaignRetrieveUpdateDestroyView
from . views import PackagesListCreateView, PackagesRetrieveUpdateDestroyView, ProductItemListCreateView, ProductItemRetrieveUpdateDestroyView
from . views import OrderItemListCreateView, OrderItemRetrieveUpdateDestroyView, PaymentListCreateView, PaymentRetrieveUpdateDestroyView

urlpatterns = [
    path('', views.api_index, name='api_index'),
    
    path('clients/', ClientListCreateView.as_view(), name='client_list_create'),
    path('payment_gateways/', Payment_gatewayListCreateView.as_view(), name = 'payment_gateway_list_create'),
    path('payment_invoices/', Payment_invoiceListCreateView.as_view(), name='payment_invoice_list_create'),
    path('whatspp/', WhatsppListCreateView.as_view(), name='whatspp_list_create'),
    path('sms/', SmsListCreateView.as_view(), name='sms_list_create'),
    path('email/', EmailListCreateView.as_view(), name='email_list_create'),
    path('contacts/', ContactListCreateView.as_view(), name='contacts_list_create'),
    path('camphaigns/', campaignListCreateView.as_view(), name='camphain_list_create'),
    path('packages/', PackagesListCreateView.as_view(), name='packages_list_create'),
    path('productitems/', ProductItemListCreateView.as_view(), name='product_item_list_create'),
    path('orders/', OrderItemListCreateView.as_view(), name='order_item_list_create_view'),
    path('payments/', PaymentListCreateView.as_view(), name='payment_list_create'),
]