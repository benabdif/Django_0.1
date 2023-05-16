from django.urls import path

from . import views as buy_views
from .views import Post_card

urlpatterns = [

    #path('sell/', views.Post_card.as_view(), name='sell'),
    path('sell/', buy_views.sell, name='sell'),
    #path('post_order/', buy_views.post_order, name='post_order'),
    path('post_order/', Post_card.as_view(), name='post_order'),


    
]