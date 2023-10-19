from django.shortcuts import render
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
from .forms import *


# Create your views here.
def index(request):
    # nationality = Hotel.objects.all().values_list('nationality')
    return render(request, 'main/base.html',)


class AccountAdd(SuccessMessageMixin, generic.CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'main/base.html'
    success_message = "تم تأمين حسابك بنجاح!"
    success_url = 'success'


def success(request):
    # nationality = Hotel.objects.all().values_list('nationality')
    return render(request, 'main/success.html',)