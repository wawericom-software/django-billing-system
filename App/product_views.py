from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single product
def product_create(request):
    if request.method == 'POST':
        form = ProductItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/home")
        else:
            form = ProductItemForm()
    form = ProductItemForm(request.POST, request.FILES)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/product_create.html", context)

#view for updating a single product

def product_update(request, pk):
    Product = get_object_or_404(ProductItem, pk=pk)
    form = ProductItemForm(request.POST, request.FILES, instance=Product)
    if request.method == 'POST':
        form = ProductItemForm(request.POST, request.FILES, instance=Product)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            form = ProductItemForm(request.POST,  request.FILES,instance=Product)
    context = {
            'form' : form,
            'Product' : Product
        }
    return render(request, "Dashboard/product_update.html", context)

#view for viewing a single product detail

def product_detail(request, pk):
    company_product = get_object_or_404(ProductItem, pk=pk)
    context = {
        'company_product' : company_product
    }
    return render(request, "Dashboard/product_detail.html", context)

#view for deleting single product

def product_delete(request, pk):
        product_delete = get_object_or_404(ProductItem, pk=pk)
        product_delete.delete()
        return redirect('/home')

#view for deleting all products
def products_delete(request):
    all_products=ProductItem.objects.all()
    all_products.delete()
    return redirect('/home')
    
#view for product details

def products_detail(request):
    company_products = ProductItem.objects.all()
    context = {
        "company_products" : company_products
    }
    return render(request, "Dashboard/products_detail.html", context)