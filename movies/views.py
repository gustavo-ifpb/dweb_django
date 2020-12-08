from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

from . import models, forms

class UserCreateView(CreateView):

    form_class = forms.UserForm
    template_name = 'users/form.html'
    success_url = reverse_lazy('movies-list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['groups'] = Group.objects.all()
        return context


class CategoryListView(ListView):

    model = models.Category
    template_name = 'movies/category/list.html'
    # paginate_by = 1


class MovieListView(ListView):

    model = models.Movie
    queryset = models.Movie.objects.filter(status=True)
    template_name = 'movies/movie/list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['categories'] = models.Category.objects.all()
        return context


class MovieDetailView(DetailView):

    model = models.Movie
    template_name = 'movies/movie/detail.html'


class MovieCreateView(LoginRequiredMixin, CreateView):

    model = models.Movie
    fields = ('name', 'status', 'obs', 'category', 'photo')
    template_name = 'movies/movie/form.html'
    success_url = reverse_lazy('movies-list')


class MovieUpdateView(UpdateView):

    model = models.Movie
    fields = ('name', 'status', 'obs', 'category')
    template_name = 'movies/movie/form.html'
    success_url = reverse_lazy('movies-list')


class MovieDeleteView(DeleteView):

    model = models.Movie
    success_url = reverse_lazy('movies-list')