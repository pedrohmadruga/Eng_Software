from django.shortcuts import render
from .models import UserCPF, UserCNPJ
from django.http import HttpResponseRedirect
from django.urls import reverse
def register(request):
    name = request.POST.get('name')
    if 'phone-number' in request.POST:
        new_user = UserCNPJ();
        new_user.name = request.POST.get('name')
        new_user.cnpj = request.POST.get('cnpj')
        new_user.phone_number = request.POST.get('phone-number')
        new_user.email = request.POST.get('email')
        new_user.password = request.POST.get('password')
        new_user.save()
    elif name:
        new_user = UserCPF()
        new_user.name = request.POST.get('name')
        new_user.cpf= request.POST.get('cpf')
        new_user.email = request.POST.get('email')
        new_user.password = request.POST.get('password')
        new_user.save()
    #return HttpResponseRedirect(reverse('home.html'))
    return render(request, 'register/register.html')

def login(request):
    return render(request, 'login/login.html')
