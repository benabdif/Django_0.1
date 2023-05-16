from django.http import HttpResponse  # we will see
from django.shortcuts import render
from django.views.generic import ListView

from .forms import land_1, my, test_t1
from .models import Addproduct, Addproduct2, Land  # this is the first steps

# Create your views here.


def fadhel(request):
    context = {
        'Addproduct2': Addproduct2.objects.all()
              
    }
    return render(request, 'buy_product/homebuy.html', context)

# def sell_1(request):
#     con = {
#         'Land': Land.objects.all()
#     }
#     return render(request, 'buy_product/post_order.html', con)

def sell(request):
    form = my()
    form1 = test_t1()
    formm = land_1()
    return render(request, 'buy_product/sell.html', {'form':form, 'form1':form1, 'formm':formm})

# def post_order(request):
#     return render(request, 'buy_product/post_order.html')

class Post_card(ListView):
    model = Land
    template_name = 'buy_product/post_order.html'
    context_object_name_1 = 'lands'
    ordering_1 = ['-date_posted']
    
    
# This for example to gied me: 


# class PostListViem(ListView):
#     model = Post
#     template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']   