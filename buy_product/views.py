from django.http import HttpResponse  # we will see
from django.shortcuts import render

from .forms import my, test_t1
from .models import Addproduct, Addproduct2  # this is the first steps

# Create your views here.


def fadhel(request):
    context = {
        'Addproduct2': Addproduct2.objects.all()
              
    }
    return render(request, 'buy_product/homebuy.html', context)

def sell(request):
    form = my()
    form1 = test_t1
    return render(request, 'buy_product/sell.html', {'form':form, 'form1':form1})