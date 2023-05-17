from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .forms import land_1, my, test_t1
from .models import Addproduct2, Land


def fadhel(request):
    context = {
        'Addproduct2': Addproduct2.objects.all()
              
    }
    return render(request, 'buy_product/homebuy.html', context)


def sell(request):
    form = my()
    form1 = test_t1()
    formm = land_1()
    return render(request, 'buy_product/sell.html', {'form':form, 'form1':form1, 'formm':formm})


class PostList(ListView):
    model = Addproduct2
    template_name = 'buy_product/post_order.html' # <app>/<model>_<viewtype>.html
    ordering = ['-date_posted_product']
