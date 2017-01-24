from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy

from app.models import Profile, Category, Item

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['login'] = AuthenticationForm
        return context

class UserCreateView(CreateView):
    template_name = "auth/user_form.html"
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
      #save the new user first
      form.save()
      #get the username and password
      username = self.request.POST['username']
      password = self.request.POST['password1']
      #authenticate user then login
      user = authenticate(username=username, password=password)
      login(self.request, user)
      return super(UserCreateView, self).form_valid(form)