
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Klient
from .forms import ClientsCreateForm, KlientsCreateForm
from django.views.generic import TemplateView , ListView , DetailView ,CreateView
from django.contrib.auth.decorators import login_required

# Create your views here.
#funkcja
@login_required
def home(request):
    context_variable = "context variable"
    return render(request, "base.html",{"context_variable": context_variable}) 
def home2(request):
    context_variable = "context variable"
    return render(request, "home2.html",{"context_variable": context_variable}) 
def home3(request):
    context_variable = "context variable"
    return render(request, "home3.html",{"context_variable": context_variable}) 

def klienci_createview(request):
    form = KlientsCreateForm(request.POST or None) #forma django przesyłana do templatki
    
    #if request.method == 'POST': 
        #  form = ClientsCreateForm(request.POST)
    if form.is_valid():
        form.save()
        #obj = Klient.objects.create(
        #    name = form.cleaned_data.get('name'),
       #     surname = form.cleaned_data.get('surname')               
       # )
        return HttpResponseRedirect("/admin")  
    if form.errors:
        print(form.errors)  
    template_name = 'klient/form.html'
    context = {"form":form}
    return render(request, template_name, context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'home4.html'
        queryset = Klient.objects.all()
        context_variable = {
            "object_list": queryset
        }
        return render(request,template_name,context_variable) 

class ContactListView(ListView):
    template_name = 'home3.html'
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Klient.objects.filter(
                Q(surname__iexact=slug) |
                Q(surname__icontains=slug)
                )
        else:
            queryset = Klient.objects.none()
        return queryset

class ContactListAll(ListView):

    queryset = Klient.objects.filter(surname__iexact="")
    template_name = 'home3.html'

class KlientDetailView(DetailView): 
    template_name = 'klient/details.html'
    queryset = Klient.objects.all()


    def get_object(self,*args,**kwargs):
        rest_id = self.kwargs.get("slug")
        obj = get_object_or_404(Klient, slug=rest_id)
        return obj

class KlientCreateView(CreateView):
    form_class = KlientsCreateForm
    template_name = "klient/form.html"
    success_url = "/home3"

