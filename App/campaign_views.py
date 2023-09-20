from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single campaign
def campaign_create(request):
    if request.method == 'POST':
        form = campaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/campaigns')
        else:
            form = campaignForm()
    form = campaignForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/campaign_create.html", context)

#view for updating a single campaign
def campaign_detail(request, pk):
    Campaign = get_object_or_404(Campaign, pk=pk)
    form = campaignForm(request.POST, instance=Campaign)
    if request.method == 'POST':
        form = campaignForm(request.POST, instance=Campaign)
        if form.is_valid():
            form.save()
            return redirect('/home/campaigns')
        else:
            form = campaignForm(request.POST, instance=Campaign)
    context = {
            'form' : form
        }
    return render(request, "Dashboard/campaign_update.html", context)

#view for viewing a single client detail

def campaign_update(request, pk):
    campaigns = get_object_or_404(Client, pk=pk)
    context = {
        'campaigns' : campaigns   
        }
    return render(request, "Dashboard/campaign_detail.html", context)

#view for deleting single campaign

def campaign_delete(request, pk):
    if request.method == 'POST':
        delete_campaign = get_object_or_404(campaign, pk=pk)
        delete_campaign.delete()
        return redirect('/home/campaigns')

#view for deleting all campaigns
def campaigns_delete(request):
    delete_campaigns = campaign.objects.all()
    delete_campaigns.delete()
    return redirect('/home/campaigns')
    
#view for campaign details

def campaigns_detail(request):
    company_campaigns = campaign.objects.all()
    context = {
        "company_campaigns" : company_campaigns
    }
    return render(request, "Dashboard/campaigns_detail.html", context)