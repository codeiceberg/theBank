from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .models import Account
from .form import AccountForm


def home(request):
    return HttpResponse('Do all things for the grace of God')


class AccountListView(ListView):
    model = Account
    context_object_name = 'accounts'
    template_name = 'account_list.html'
# def account(request):
#     account_list = Account.objects.all()
#     return render(request, 'account.html', {'accounts': account_list})


class AccountDetailsView(DetailView):
    model = Account
    context_object_name = 'account'
    template_name = 'account_details.html'
# def detail(request, id):
#     try:
#         account_details = Account.objects.get(id=id)
#     except Account.DoesNotExist:
#         raise Http404('Account does not exist!')
#     return render(request, 'details.html', {'account': account_details})


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
