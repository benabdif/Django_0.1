from django.http import HttpResponse  # we will see
from django.shortcuts import render

from .models import Addproduct, Addproduct2  # this is the first steps

# Create your views here.


def fadhel(request):
    context = {
        'Addproduct2': Addproduct2.objects.all()
              
    }
    return render(request, 'buy_product/homebuy.html', context)

def sell(request):
    return render(request, 'buy_product/sell.html')