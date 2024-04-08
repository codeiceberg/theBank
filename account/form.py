from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from .models import Account, Transaction


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'account_type': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'account_balance': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }
        labels = {
            'account_type': 'Type',
            'account_balance': 'Balance',
        }
        fields = ['name', 'account_type', 'account_balance', 'is_activate']

    def clean_account_balance(self):
        account_balance = self.cleaned_data['account_balance']
        if account_balance < 100:
            raise ValidationError('Initial balance should be $100.00 or more')
        return account_balance
