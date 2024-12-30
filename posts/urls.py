from django.urls import path
from .views import PostList, PostCreate, PostDetail, PostEdit, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('add/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]