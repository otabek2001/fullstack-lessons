from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView

from .models import Category


# Create your views here.

class CategoryList(TemplateView):
    template_name = 'categories/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories/category_new.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['pk'])
        return context