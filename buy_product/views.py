from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

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



# This is to create a model of details

class PostDetail(DetailView):
    model = Addproduct2
    template_name = 'buy_product/post_details1.html'
    


class PostCreate(CreateView):
    model = Addproduct2
    fields = ['price', 'name', 'description']
    template_name = 'buy_product/post_details1.html'
    
  
# Example of Dashbord 
num = 10
def mynum(num):
    for x in range(num):
        result = x * 'Fadhel'
    return result

new_in = mynum

def Dashbord(request):
    num = 10
    for x in range(num):
        result  = x * 'Fadhel'
    
    
             
   
    return render(request,'buy_product/dashbord.html', {'name':'Fadhel 0010'})
    