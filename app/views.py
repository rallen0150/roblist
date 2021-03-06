from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, FormView, UpdateView
from app.forms import ContactForm

from django.urls import reverse_lazy

from app.models import Profile, Category, Item, Comment, Reply

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['login'] = AuthenticationForm
        return context

class UserCreateView(FormView):
    template_name = "auth/user_form.html"
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('profile_update_view')

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

class CategoryCreateView(CreateView):
    model = Category
    fields = ('item_type', )
    success_url = reverse_lazy('category_list_view')

class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

class ItemCreateView(CreateView):
    model = Item
    fields = ('name', 'picture', 'price', 'description')
    success_url = reverse_lazy('category_list_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.category = Category.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.filter(category=self.kwargs['pk'])
        return context

class ItemDetailView(DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = Item.objects.get(id=self.kwargs['pk'])
        return context

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ('first_name', 'last_name', 'email', 'image')
    success_url = reverse_lazy('category_list_view')

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

class ProfileDetailView(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['details'] = Profile.objects.get(id=self.kwargs['pk'])
        return context

class CommentCreateView(CreateView):
    model = Comment
    fields = ('comment', )

    def get_success_url(self, **kwargs):
        return reverse_lazy('item_detail_view', args=[int(self.kwargs['pk'])])

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.item_commented = Item.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ('comment', )

    def get_success_url(self, **kwargs):
        x = Comment.objects.get(id=self.kwargs['pk']).item_commented.id
        return reverse_lazy('item_detail_view', args=[x])

class ReplyCreateView(CreateView):
    model = Reply
    fields = ('reply', )

    def get_success_url(self, **kwargs):
        x = Comment.objects.get(id=self.kwargs['pk']).item_commented.id
        return reverse_lazy('item_detail_view', args=[x])

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.comment = Comment.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class ReplyUpdateView(UpdateView):
    model = Reply
    fields = ('reply', )

    def get_success_url(self, **kwargs):
        x = Reply.objects.get(id=self.kwargs['pk']).comment.item_commented.id
        return reverse_lazy('item_detail_view', args=[x])

class ContactView(TemplateView):
    template_name = 'contact_me.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = ContactForm()
        return context

class SendMailView(FormView):
    template_name = 'contact_me.html'
    success_url = reverse_lazy("category_list_view")
    form_class = ContactForm

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
