from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from django.views import generic

from .forms import CustomUserCreationForm

# Create your views here.


# def SignupPageView(request):
#     user = get_user_model()
#
#     username = request.POST.get('username')
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#
#     user.username = username
#     user.email = email
#     user.set_password = password
#
#     user.save()

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



