from django.conf import settings
from django.db import models
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.urls import reverse


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    contact = models.IntegerField(blank=True, null=True)
    Email = models.EmailField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    password = models.IntegerField(blank=True, null=True)
    confirm_password = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.first_name
    
    
class router_hotspot(models.Model):
    name = models.CharField(max_length=255)
    area_name = models.CharField(max_length=255)
    ip_adressv4 = models.GenericIPAddressField()
    status = models.BooleanField()
    start_date = models.DateTimeField(auto_now=True)
    
    
class router(models.Model):
    name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    ip_adressv4 = models.GenericIPAddressField()
    status = models.BooleanField()
    start_date = models.DateTimeField(auto_now=True)
    

class payment_gateway(models.Model):
    name = models.CharField(max_length=255)
    logo = models.FileField(null=True, blank=True)
    api_key = models.CharField(max_length=255)
    api_client = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class payment_invoice(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True,blank=True, null=True)
    client_name = models.ForeignKey(Client, on_delete= models.CASCADE)
    message_template = models.TextField(max_length=12000)
    method = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[('paid', 'Paid'),('pending','Pending')], blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class sms(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    api_client = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    
class whatspp(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    api_client = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    

class email(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    api_client = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    

class contacts(models.Model):
    add_contact = models.IntegerField(null=True, blank=True)
    upload_contact_file = models.IntegerField(null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(auto_now=True)

class campaign(models.Model):
    name = models.CharField(max_length=255)
    phone_contact = models.ForeignKey(contacts,on_delete=models.CASCADE,null=True, blank=True)
    message_template = models.TextField()
    status = models.CharField(max_length=255, choices = [('Active', 'Active'), ('Inactive', 'Inactive')])
    date = models.DateTimeField(auto_now=True)
      

class Packages(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    duration = models.CharField(max_length=255, null=True, blank=True)
    description=models.TextField(max_length=255, null=True, blank=True)
    
#Item model, for storing different items to be sold
class ProductItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to='upload',blank=True, null=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("core:product", kwargs={'slug': self.slug})


    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={'slug': self.slug})


    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={'slug': self.slug})
    
    class Meta():
        pass


#Order Item, checks on a particular item if ordered
class OrderItem(models.Model):
    user = models.ForeignKey(Client,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


    def get_total_item_price(self):
        return self.quantity * self.item.price


    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price


    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()


    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


#Order Model, Details on the Order made
class Order(models.Model):
    METHOD_CHOICES = (
        ("plan", 'plan'),
        ('fixed', 'fixed')
    )
    user = models.ForeignKey(Client,on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    billing_address = models.ForeignKey('Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    method = models.CharField(max_length=200,choices=METHOD_CHOICES, null=True, blank=True)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user}"
        

#Address Model
class Address(models.Model):
    CHOICES = (
        ('Kenya', 'Kenya'),
        ('Uganda', 'Uganda'),
    )
    user = models.ForeignKey(Client,on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country =models.CharField(max_length=255,choices=CHOICES)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=255)
    default = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user}"


    class Meta:
        verbose_name_plural = 'Addresses'


#Payment Model Using stripe
class Payment(models.Model):
    payment_method = models.ForeignKey(payment_gateway, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(Client,on_delete=models.CASCADE, blank=True, null=True)
    invoice = models.ForeignKey(payment_invoice, on_delete=models.CASCADE,null=True, blank=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user


#Coupon Model
class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()
    def __str__(self):
        return self.code


#Refund Model
class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()


    def __str__(self):
        return f"{self.pk}"


class product(models.Model):
    pass