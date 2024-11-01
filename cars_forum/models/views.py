from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Car, Comment, User

# Create your views here.

class CarCreate(LoginRequiredMixin,CreateView):
    pass

class CarEdit(LoginRequiredMixin, UpdateView):
    pass

class CarDelete(LoginRequiredMixin, DeleteView):
    pass

class CarList(ListView):
    pass
