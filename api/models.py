from django.db import models
from tastypie.resources import ModelResource
from account.models import Account


class AccountResource(ModelResource):
    class Meta:
        queryset = Account.objects.all()
        resource_name = 'account'
        excludes = ['create_date', 'resource_uri',]
