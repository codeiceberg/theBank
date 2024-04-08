from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Account(models.Model):
    ACCOUNT_TYPE_CHOICES = [('Savings', 'Savings'), ('Payroll', 'Payroll')]

    name = models.CharField(max_length=255)
    account_type = models.CharField(
        max_length=1, choices=ACCOUNT_TYPE_CHOICES, default='Savings')
    account_balance = models.BigIntegerField()
    is_activate = models.BooleanField()
    create_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='account')

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICE = [
        ('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(
        max_length=1, choices=TRANSACTION_TYPE_CHOICE, default='D')
    transaction_amout = models.BigIntegerField()
    running_balance = models.BigIntegerField()
    transaction_date = models.DateField(auto_now_add=True)
