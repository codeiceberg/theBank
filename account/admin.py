from django.contrib import admin
from .models import Account, Transaction


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_type',
                    'account_balance', 'create_date', 'user',)
    exclude = ('create_date',)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'transaction_type',
                    'transaction_amout', 'running_balance', 'transaction_date', )


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
