from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.conf import settings
from .utils import get_random_string

# Create your models here.

User = settings.AUTH_USER_MODEL

class Profile(models.Model): # rozszerzenie modelu usera
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Relacja jeden do jeden id profile do user:user(id)
    owner = models.BooleanField(default=True)  # czy właściciel firmy
    kod_kon = models.IntegerField(null=True,blank=True,) #kod firmy
    aktywny = models.BooleanField(default=True) # określa mozliwosc korzystania z systemu
    kod_aktywacyjny = models.CharField(null=True,blank=True,max_length=20) 

    def __str__(self):
        return self.user.username
    
    def activation_mail(self):
        
        if not self.user.is_active:
            
            self.kod_aktywacyjny =  get_random_string(16)
            self.save()
            print('Wysylam maila z kodem aktywacyjnym ;)  : ',self.kod_aktywacyjny)
            sent_email = False 
            return sent_email
     
        
       



def post_save_user_receiver(sender, instance, created, **kwargs):
    if created:
         profile, is_created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=User)
