from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .models import Account, Transaction
from .form import AccountForm, TransactionForm


def home(request):
    return HttpResponse('Do all things for the grace of God')


# def account(request):
#     account_list = Account.objects.all()
#     return render(request, 'account.html', {'accounts': account_list})
class AccountListView(ListView):
    model = Account
    context_object_name = 'accounts'
    template_name = 'account_list.html'


# def detail(request, id):
#     try:
#         account_details = Account.objects.get(id=id)
#     except Account.DoesNotExist:
#         raise Http404('Account does not exist!')
#     return render(request, 'details.html', {'account': account_details})
class AccountDetailsView(DetailView):
    model = Account
    context_object_name = 'account'
    template_name = 'account_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = self.get_object()
        transactions = Transaction.objects.filter(account=account)
        context['transactions'] = transactions
        return context


class AccountCreateView(CreateView):
    model = Account
    # fields = ['name', 'account_type', 'account_balance', 'is_activate']
    form_class = AccountForm
    template_name = 'account_form.html'
    success_url = '/account/'
    login_url = '/admin'

    # inject the current user before saving data by overingding the form.
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'account_form.html'
    success_url = '/account/'


class AccountDeleteView(DeleteView):
    model = Account
    form_class = AccountForm
    template_name = 'account_delete.html'
    success_url = '/account/'


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transaction_form.html'
    success_url = '/account/'

    def form_valid(self, form):
        # Extract account_id from URL kwargs
        account_id = self.kwargs['pk']

        # Get the Account object using account_id
        account = Account.objects.get(id=account_id)

        # Assign the account to the transaction
        form.instance.account = account

        # Update account balance based on transaction type
        amount = form.cleaned_data['transaction_amout']
        transaction_type = form.cleaned_data['transaction_type']

        # Update account balance based on transaction type
        if transaction_type == 'D':
            account.account_balance += amount
        elif transaction_type == 'W':
            account.account_balance -= amount

        # Save the updated balance before saving the transaction
        account.save()

        # Proceed with the form validation
        return super().form_valid(form)
