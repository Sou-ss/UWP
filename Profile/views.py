

from django.views import View
from .forms import RegisterUser,EmailValidationForm
from django.views.generic import TemplateView , ListView , DetailView ,CreateView
from .models import Profile
from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your views here.
def Activated(request,*args,**kwargs):
    return render(request,"registration/activated.html")

def EmailCodeValidation(request,*args,**kwargs):
    form = EmailValidationForm(request.POST or None)
    if form.is_valid():       
        return redirect('/register/validation/activated')
    return render(request,"registration/validation.html",{"form":form}) 

class Register(CreateView):

    form_class = RegisterUser
    template_name = "registration/registration.html"
    success_url = '/register/validation'

class ProfileDetailView(LoginRequiredMixin,DetailView):
      def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
    

