from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Item

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="email", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),required=True)
    first_name = forms.CharField(label="first_name",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"First Name"}))
    last_name = forms.CharField(label="last_name",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Last Name"}))
    
    class Meta:
        model = User
        fields = ("first_name","last_name","email","username","password1","password2")
    
    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control bg-blue-700'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = None
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = 'Password'
        self.fields['password1'].help_text = None
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = ''
        self.fields['password2'].label = 'Confirm password'
        self.fields['password2'].help_text = None

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))
    
    class Meta:
        model = User
        fields = ('username','password')

class ItemForm(forms.ModelForm):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    quantity = forms.IntegerField(min_value=1,max_value=20,required=True)
    type_product = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    
    class Meta:
        model = Item
        fields = ('name','quantity','type_product')