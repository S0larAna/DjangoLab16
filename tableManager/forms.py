from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
import re

pattern_name = re.compile(r'^[А-Я][а-я]*$')

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
            super(JewelryForm, self).__init__(*args, **kwargs)
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

    def clean(self):

        # data from the form is fetched using super function
        super(CreateUserForm, self).clean()

        # extract the username and text field from the data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        patronymic = self.cleaned_data.get('patronymic')
        text = self.cleaned_data.get('text')

        # conditions to be met for the username length
        if not bool(pattern_name.match(first_name)):
            self._errors['first_name'] = self.error_class([
                'Неверный формат'])
        if not bool(pattern_name.match(last_name)):
            self._errors['last_name'] = self.error_class([
                'Неверный формат'])
        if not bool(pattern_name.match(patronymic)):
            self._errors['patronymic'] = self.error_class([
                'Неверный формат'])

        # return any errors if found
        return self.cleaned_data

