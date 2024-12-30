from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField("Sarlavha", max_length=255)
    summary = models.CharField("Qisqa mazmuni" ,max_length=200, blank=True)
    content = models.TextField("Maqola")
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ManyToManyField('categories.Category', related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
