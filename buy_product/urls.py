from django.urls import path

from . import views as buy_views
from .views import PostList

urlpatterns = [

    path('sell/', buy_views.sell, name='sell'),
    #path('post_order/', PostListView1.as_view(), name='post_order'),
    path('ad/', PostList.as_view(), name='post_order'),
    path('add/', buy_views.fadhel, name= 'add'),
    
]