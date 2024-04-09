from django.test import TestCase

# tests.py
import pytest
from django.test import RequestFactory
from django.contrib.auth.models import User
from .views import AccountListView, AccountDetailsView, AccountCreateView, AccountUpdateView, AccountDeleteView, TransactionCreateView
from .models import Account, Transaction
from .form import AccountForm, TransactionForm


@pytest.fixture
def user():
    return User.objects.create_user(username='test_user', password='test_password')


@pytest.fixture
def account(user):
    return Account.objects.create(name='Test Account', account_type='S', account_balance=10, is_activate=True, user=user)


@pytest.mark.django_db
def test_account_details_view(account):
    request = RequestFactory().get('/')
    response = AccountDetailsView.as_view()(request, pk=account.pk)
    assert response.status_code == 200


@pytest.mark.django_db
def test_account_form_valid():
    form_data = {
        'name': 'Test Account',
        'account_type': 'S',
        'account_balance': 150,
        'is_activate': True
    }
    form = AccountForm(data=form_data)
    assert form.is_valid()  # Check if form is valid


@pytest.mark.django_db
def test_account_form_invalid():
    form_data = {
        'name': 'Test Account',
        'account_type': 'S',
        'account_balance': 50,  # Initial balance less than $100
        'is_activate': True
    }
    form = AccountForm(data=form_data)
    assert not form.is_valid()  # Check if form is invalid
    # Check if 'account_balance' field has error
    assert 'account_balance' in form.errors
