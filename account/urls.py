from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountListView.as_view(), name='account_list'),
    # path('accounts/', views.account, name='account'),

    path('new', views.AccountCreateView.as_view(), name='account_new'),

    path('<int:pk>', views.AccountDetailsView.as_view(), name='account_detail'),
    # path('<int:id>', views.detail, name='account_detail'),

    path('<int:pk>/edit', views.AccountUpdateView.as_view(), name='account_update'),

    path('<int:pk>/delete', views.AccountDeleteView.as_view(), name='account_delete'),



]
