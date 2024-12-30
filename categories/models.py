from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField("Kategoriya", max_length=255)
    description = models.TextField("Tavsif", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])