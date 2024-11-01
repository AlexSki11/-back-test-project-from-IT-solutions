from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Car, Comment, User
from .forms import CarCreateForm, CommentCreateForm

# Create your views here.

class CarCreate(LoginRequiredMixin, CreateView):
    form_class = CarCreateForm
    model = Car
    template_name = 'car_templates/car_create.html'

    def form_valid(self, form):
        car_object = form.save(commit=False)
        car_object.owner = self.request.user
        car_object.save()

        return HttpResponseRedirect(car_object.get_absolute_url())

class CarEdit(LoginRequiredMixin, UpdateView):
    form_class = CarCreateForm
    model = Car
    template_name = 'car_templates/car_create.html'
    raise_exception = True

    def get(self, request, *args, **kwargs):
        get = super().get(request, *args, **kwargs)
        if self.object.owner != request.user:
            raise PermissionDenied
        return get
    
    def form_valid(self, form):
        car_object = form.save(commit=False)
        car_object.update_date()
        car_object.save()

        return HttpResponseRedirect(car_object.get_absolute_url())
    
    
    


class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'car_templates/car_delete.html'
    success_url = reverse_lazy('car_list')

    def get(self, request, *args, **kwargs):
        get = super().get(request, *args, **kwargs)
        if self.object.owner != request.user:
            raise PermissionDenied
        return get
    


class CarList(ListView):
    model = Car
    template_name = 'car_templates/car_list.html'
    context_object_name = 'cars'
    ordering = '-created_at'

class CarDetail(DetailView):
    model = Car
    template_name = 'car_templates/car_detail.html'
    context_object_name = 'car'
