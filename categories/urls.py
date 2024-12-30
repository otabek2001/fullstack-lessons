from django.urls import path
from .views import CategoryList, CategoryCreateView, CategoryDetailView

urlpatterns = [
    path('', CategoryList.as_view(), name='category_list'),
    path('add/', CategoryCreateView.as_view(), name='category_add'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]