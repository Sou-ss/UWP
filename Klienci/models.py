
from datetime import datetime
from django.db import models
from django.db.models.signals import pre_save, post_save
from Klienci.utils import unique_slug_generator
from django.conf import settings

# Create your models here.
#auto_now -  each time value is modified the field is updated
#auto_now_add - time value is modified only when field is created
User = settings.AUTH_USER_MODEL

class Klient(models.Model): # model klienta
    owner          = models.ForeignKey(User,on_delete=models.CASCADE)
    name           = models.CharField(max_length=20)
    surname        = models.CharField(max_length=20,null=True,blank=True)
    dogs_name      = models.CharField(max_length=20,null=True,blank=True)
    comments       = models.CharField(max_length=200,null=True,blank=True)
    dogs_race      = models.CharField(max_length=20,null=True,blank=True)
    timestamp      = models.DateTimeField(auto_now_add=True,null=True)
    updated        = models.DateTimeField(auto_now=True,null=True)
    my_date_field  = models.DateTimeField(auto_now=False,auto_now_add=False,default=datetime.today)
    slug           = models.SlugField(blank=True,null=True)

    def __str__(self):
        return self.name + ' ' + self.surname

    @property 
    def title(self):
        return (self.name + self.surname)

def rl_pre_save_signal_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        
        


#def rl_post_save_signal_receiver(sender,instance,*args,**kwargs):
    #print('saved')
    


pre_save.connect(rl_pre_save_signal_receiver,sender=Klient)

#post_save.connect(rl_post_save_signal_receiver, sender=Klient)
