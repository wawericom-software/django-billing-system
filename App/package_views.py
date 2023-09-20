from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single package
def package_create(request):
    if request.method == 'POST':
        form = PackagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
        else:
            form = PackagesForm()
    form = PackagesForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/package_create.html", context)

#view for updating a single package

def package_update(request, pk):
    package = get_object_or_404(Packages, pk=pk)
    form = PackagesForm(request.POST, instance=package)
    if request.method == 'POST':
        form = PackagesForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            form = PackagesForm(request.POST, instance=package)
    context = {
            'form' : form,
            'package' : package
        }
    return render(request, "Dashboard/package_update.html", context)

#view for viewing a single Packages detail

def package_detail(request, pk):
    company_package = get_object_or_404(Packages, pk=pk)
    context = {
        'company_package' : company_package
    }
    return render(request, "Dashboard/package_detail.html", context)

#view for deleting single package

def package_delete(request, pk):
    delete_package = get_object_or_404(Packages, pk=pk)
    delete_package.delete()
    return redirect('/home')

#view for deleting all packages
def packages_delete(request):
    delete_packages =  Packages.objects.all.delete()
    delete_packages.delete()
    return redirect('/')
    
#view for package details

def packages_detail(request):
    company_packages = Packages.objects.all()
    context = {
        "company_packages" : company_packages
    }
    return render(request, "Dashboard/packages_detail.html", context)