from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


# Create your views here.

class PostList(TemplateView):
    template_name = 'posts/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        return context

class PostDelete(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
class PostEdit(UpdateView):
    model = Post
    template_name = 'posts/post_edit.html'
    fields = ['title', 'summary', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
class PostCreate(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    fields = ['title', 'summary', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.created_by = self.request.user
        return super().form_valid(form)
