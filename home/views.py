from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/account/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('account_list')
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = 'login.html'


class LoginOutterfaceView(LogoutView):
    template_name = 'logout.html'


def home(request):
    return render(request, 'welcome.html', {'today': datetime.today()})
