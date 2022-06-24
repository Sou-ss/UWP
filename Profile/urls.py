from django.urls import path
from .views import (Register,ProfileDetailView,EmailCodeValidation,Activated)

app_name = 'Profile'
urlpatterns = [
    
    path('', Register.as_view(),name='register'),
    path('validation/', EmailCodeValidation,name='email_validation'),
    path('validation/activated', Activated,name='activated'),
    path('profile/<int:pk>',ProfileDetailView.as_view()),
   
    
]