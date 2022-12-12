from django.shortcuts import render
from . import models, forms
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

# Create your views here.
class AccountView(ListView):
    model = models.Account
    template_name = 'core/home.html'

    def get_context_data(self, *args, **kwargs):
        owner_account = models.Account.objects.filter(owner_id= self.request.user.id)
        context = super(AccountView, self).get_context_data(*args, **kwargs)
        context["owner_account"] = owner_account
        return context 


def Expenses(request, account_id):
    balance = models.Account.objects.get(id=account_id)
    savings = 0.25 * balance.balance
    house = 0.25 * balance.balance
    jaiye = 0.05 *  balance.balance
    grocery = 0.20 * balance.balance
    wardrobe = 0.10 * balance.balance
    unforseen = 0.15 * balance.balance

    context = {'house':house, 'balance': balance, 'jaiye': jaiye, 'unforseen':unforseen, 'closet':wardrobe, 'savings': savings, 'grocery':grocery}

    return render(request, 'core/account.html', context)

class CreateBalance(CreateView):
    model = models.Account
    template_name = 'core/create_account.html'
    form_class = forms.AccoutnForm
    success_url = reverse_lazy('account')

class SignUpView(CreateView):
    form_class = forms.SignUpForm
    template_name = 'core/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        return super().form_valid(form)
