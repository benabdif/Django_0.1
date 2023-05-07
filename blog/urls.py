from django.urls import path

from . import views
from .views import (PostCreateView, PostDeleteViem, PostDetailViem,
                    PostListViem, PostUpdateView)

urlpatterns = [
    # path('', PostListViem.as_view(), name='blog-home'), This if I want to delete it
    path('', views.about, name='blog-about'),
    path('home/', PostListViem.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailViem.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteViem.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    
    
    
    
    #path('about/', views.about, name='blog-about'), This if I want to delete
]

