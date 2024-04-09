from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Account(models.Model):
    ACCOUNT_TYPE_CHOICES = [('S', 'Savings'), ('P', 'Payroll')]

    name = models.CharField(max_length=255)
    account_type = models.CharField(
        max_length=1, choices=ACCOUNT_TYPE_CHOICES, default='S')
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)
    is_activate = models.BooleanField()
    create_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='account')

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICE = [
        ('D', 'Deposit'), ('W', 'Withdrawal')]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(
        max_length=1, choices=TRANSACTION_TYPE_CHOICE, default='D')
    transaction_amout = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
