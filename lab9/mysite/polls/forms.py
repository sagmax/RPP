from django import forms
from .models import Item, Cashier, Store, Check, Sale
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        labels = {
            'name': 'Тип светофора',
        }


class CashierForm(forms.ModelForm):
    class Meta:
        model = Cashier
        fields = ['name']
        labels = {
            'name': 'Название светофора',
        }


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'address']
        labels = {
            'name': 'Регион',
            'address': 'Город',
        }


class CheckForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['cashier', 'date_time', 'total_sum', 'store']
        labels = {
            'cashier': 'Название',
            'date_time': 'Дата и время',
            'total_sum': 'Кол-во машин',
            'store': 'Регион',
        }
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'total_sum': forms.NumberInput(attrs={
                'step': 10,
                'min': 0,
                'max': 999999,
            })
        }


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['check_id', 'item', 'quantity']
        labels = {
            'check_id': 'ID отчета',
            'item': 'Тип',
            'quantity': 'Количество',
        }
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']