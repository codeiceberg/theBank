from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from .models import Account, Transaction


class AccountForm(forms.ModelForm):
    ACCOUNT_TYPE_CHOICES = [('S', 'Savings'), ('P', 'Payroll')]
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Account
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'account_balance': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
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


class TransactionForm(forms.ModelForm):
    TRANSACTION_CHOICES = [
        ('D', 'Deposit'), ('W', 'Withdrawal'),]

    transaction_type = forms.ChoiceField(choices=TRANSACTION_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Transaction
        widgets = {
            # 'transaction_type': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'transaction_amout': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
        }
        labels = {
            'transaction_type': 'Type',
            'transaction_amout': 'Amount',
        }
        fields = ['transaction_type', 'transaction_amout', ]
