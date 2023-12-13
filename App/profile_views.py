from django.shortcuts import get_object_or_404, render, redirect
from . models import User
from . forms import UsersForm
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy

class profile_viewsCreateView(CreateView):
    model = User 
    template_name = "profile_view_form.html"
    form_class = UsersForm
    success_url = reverse_lazy("profile_view")

class profile_viewsUpdateView(UpdateView):
    model = User 
    template_name = "profile_view_form_update.html"
    form_class = UsersForm
    success_url = reverse_lazy("profile_view")

class profile_viewsListView(ListView):
    model = User 
    template_name = "profile_view.html"
    context_object_name = "profile_views"

class profile_viewsDetailView(DetailView):
    model = User 
    template_name = "profile_view_detail.html"
    context_object_name = "profile_view"

class profile_viewsDeleteView(DeleteView):
    model = User 
    template_name = "profile_confirm_delete.html"
    success_url = reverse_lazy("profile_view")
