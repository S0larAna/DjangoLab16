from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].label = 'First Name'
        self.fields['secondname'].label = 'Second Name'
        self.fields['patronymic'].label = 'Patronymic'
        self.fields['phone'].label = 'Phone'
        self.fields['checking_account'].label = 'Checking Account'
        self.fields['address'].label = 'Address'

class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)
        self.fields['address'].label = 'Address'
        self.fields['opened'].label = 'Opened'

class JewelryForm(ModelForm):
    class Meta:
        model = Jewelry
        fields = '__all__'
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'})
        }

        def __init__(self, *args, **kwargs):
            super(StoreForm, self).__init__(*args, **kwargs)
            self.fields['type'].label = 'Type'
            self.fields['defects'].label = 'Defects'
            self.fields['date'].label = 'Date'
            self.fields['price'].label = 'Price'
            self.fields['store'].label = 'Store'
            self.fields['client'].label = 'Client'

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'patronymic', 'email', 'password1', 'password2']


