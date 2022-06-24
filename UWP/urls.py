"""UWP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from Profile.views import Register
from Klienci.views import (
    KlientCreateView,
    home,
    home2,
    home3,
    ContactView,
    ContactListView,
    ContactListAll,
    KlientDetailView,
    klienci_createview,
)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', home),
    path('home2/', home2),
    path('home3/<slug:slug>/', ContactListView.as_view()),   
    path('home3/', KlientDetailView.as_view()),
    path('home4/', ContactView.as_view()),
    path('details/<slug:slug>', ContactListView.as_view()),
    path('create/',KlientCreateView.as_view()),
    path('items/', include('ItemsApp.urls',namespace='ItemsApp')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/',include('Profile.urls',namespace='Profile')),
    

    

    
]
