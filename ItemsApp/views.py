from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView,DetailView,CreateView,UpdateView


from .models import Item
from .forms import ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



class ItemListView(LoginRequiredMixin,ListView):
    login_url = '/accounts/login'
        
    def get_queryset(self):

        return Item.objects.filter(Q(user=self.request.user)) 

class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemCreateView(CreateView):
    def get_queryset(self):
        form_class = ItemForm
        return Item.objects.filter(user=self.request.user)

class ItemUpdateView(UpdateView):
    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)