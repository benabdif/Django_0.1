from django.urls import path

from . import views as buy_views
from .views import PostCreate, PostDetail, PostList

urlpatterns = [

    path('sell/', buy_views.sell, name='sell'),
    path('ad/', PostList.as_view(), name='post_order'),
    path('post_info/<int:pk>/', PostDetail.as_view(), name='post_info'), # for HTML use
    path('post_info/new/<int:pk>/', PostCreate.as_view(), name='post_creat_View'), # New for create
    path('add/', buy_views.fadhel, name= 'add'),    
    path('dash/', buy_views.Dashbord, name= 'dash'),    
    
]



    #path('post/<int:pk>/', PostDetailViem.as_view(), name='post-detail'),
