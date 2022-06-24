
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import Profile


User = get_user_model()



class EmailValidationForm(forms.ModelForm):
     
    kod_aktywacyjny = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Wklej kod aktywacyjny','class':'un'}))
    class Meta:
        model = Profile
        fields = [
            'kod_aktywacyjny'
        ]
        
    def clean_kod_aktywacyjny(self):
        kod = self.cleaned_data.get('kod_aktywacyjny')
        qs = Profile.objects.filter(kod_aktywacyjny__iexact=kod)
        print('wprowadzony kod to',kod)
        if qs.exists():
            qs = Profile.objects.get(kod_aktywacyjny=kod)
            qs.user.is_active = True #aktywacja konta
            print(qs.user.is_active)
            qs.user.save()
        else:
            raise forms.ValidationError('Podany kod jest niepoprawny')
        return kod

class RegisterUser(forms.ModelForm):
    password1 = forms.CharField( label='', widget=forms.PasswordInput(attrs={'placeholder':'Hasło','class':'pass '}),validators=[validate_password])
    password2 = forms.CharField( label='', widget=forms.PasswordInput(attrs={'placeholder':'Potwierdź hasło','class':'pass '}))
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={'placeholder':'E-mail','class':'un '}))
    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Imię','class':'un '}))
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Login','class':'un '}))
    last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Nazwisko','class':'un '}))
    class Meta:
        model = User
        fields = [      
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            
        ]
   
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Ten adres e-mail jest już zajęty")
        return email
  


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Podane hasła nie są identyczne")
        return password2
    def save(self,commit=True):
        user = super(RegisterUser,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        
        if commit:
            user.save()
            user.profile.activation_mail()
        return user


    


